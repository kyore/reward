from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from user.models import User, Division
from .forms import UserCreateForm, SupervisorCreateForm, HrCreateForm


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        if user:
            login(self.request, user=user)

        return super(LoginView, self).form_valid(form)


def logout_view(request):
    logout(request)

    return redirect('user:login')


class DivisionCreateView(generic.CreateView):
    model = Division
    fields = "__all__"
    success_url = reverse_lazy('main:home')


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('main:home')


class SupervisorCreateView(generic.CreateView):
    model = User
    form_class = SupervisorCreateForm
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        ctx = super(SupervisorCreateView, self).get_context_data(**kwargs)
        ctx['user_type'] = 'Удирдлага'

        return ctx


class HrCreateView(generic.CreateView):
    model = User
    form_class = HrCreateForm
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        ctx = super(HrCreateView, self).get_context_data(**kwargs)
        ctx['user_type'] = 'Хүний нөөц'

        return ctx
