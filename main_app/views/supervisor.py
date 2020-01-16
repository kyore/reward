from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from main_app.forms import SupervisorRatingCreateFormSet
from main_app.models import Rating


@method_decorator(login_required, name='dispatch')
class SupervisorHomeView(generic.TemplateView):
    template_name = 'dashboard/supervisor.html'

    def get_context_data(self, **kwargs):
        ctx = super(SupervisorHomeView, self).get_context_data(**kwargs)

        return ctx

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_employee:
            return redirect(reverse_lazy('main:home'))
        elif request.user.is_hr:
            return redirect(reverse_lazy('main:home-hr'))

        return super(SupervisorHomeView, self).dispatch(request, *args, **kwargs)


class SupervisorUserRatingList(generic.ListView):
    template_name = 'main/supervisor_user_rating_list.html'

    def get_queryset(self):
        queryset = Rating.objects.filter(supervisor=self.request.user.supervisor)

        return queryset

class DivisionUserList(generic.ListView):
    template_name = 'main/supervisor_user_list.html'

    def get_queryset(self):
        user = self.request.user
        user_list = user.division.employees.all()

        return user_list


def supervisor_rating_view(request):
    formset = SupervisorRatingCreateFormSet()

    if request.POST:
        formset = SupervisorRatingCreateFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                form.instance.supervisor = request.user.supervisor
                form.save()

        return HttpResponse("SUccess")

    return render(request, 'main/supervisor_rating_create.html', {'formset': formset})
