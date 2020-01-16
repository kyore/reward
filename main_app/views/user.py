from datetime import datetime

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from main_app.forms import OwnRatingFormSet
from main_app.models import OwnRating
from utils.utils import get_season


class UserHomeView(generic.TemplateView):
    template_name = 'dashboard/employee.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('user:login'))
        elif request.user.is_supervisor:
            return redirect(reverse_lazy('main:home-sp'))
        elif request.user.is_hr:
            return redirect(reverse_lazy('main:home-hr'))

        return super(UserHomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(UserHomeView, self).get_context_data(**kwargs)
        user = self.request.user

        cluster = {
            '1-р улирал': [1, 2, 3],
            '2-р улирал': [4, 5, 6],
            '3-р улирал': [7, 8, 9],
            '4-р улирал': [10, 11, 12]
        }

        season = get_season(datetime.today())

        results = []

        for month in cluster[season]:
            data = {
                'score': user.get_month_score(month),
                'month': month,
                'list': user.get_month_rating_result(month),
                'strlist': str(user.get_month_rating_result(month)).strip('[]')
            }
            results.append(data)

        ctx['results'] = results
        # Улирлын эцэс
        season_result = 0
        for result in results:
            season_result += result['score']

        ctx['season_name'] = season
        ctx['season_result'] = season_result / 3

        return ctx


class UserOwnRatingList(generic.ListView):
    model = OwnRating
    template_name = 'main/user_rating_list.html'


def user_create_rating(request):
    formset = OwnRatingFormSet()

    if request.method == 'POST':
        formset = OwnRatingFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                form.instance.user = request.user
                form.save()

            return redirect('main:user-rating-list')

    return render(request, 'main/user_create_rating.html', {'formset': formset})
