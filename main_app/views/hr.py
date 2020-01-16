from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from main_app.forms import HrRatingCreateFormSet


@method_decorator(login_required, name='dispatch')
class HrHomeView(generic.TemplateView):
    template_name = 'dashboard/hr.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_supervisor:
            return redirect(reverse_lazy('main:home-sp'))
        elif request.user.is_employee:
            return redirect(reverse_lazy('main:home'))

        return super(HrHomeView, self).dispatch(request, *args, **kwargs)


def hr_rating_view(request):
    formset = HrRatingCreateFormSet()

    if request.POST:
        formset = HrRatingCreateFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                form.instance.hr = request.user.hr
                form.save()

        return HttpResponse("Success")

    return render(request, 'main/hr_rating_create.html', {'formset': formset})
