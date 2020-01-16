from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User, Division, Supervisor, Hr


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'salary', 'position', 'division')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.is_employee = True

        if commit:
            user.save()

        return user


class SupervisorCreateForm(UserCreateForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'salary', 'position', 'division')

    def save(self, commit=True):
        user = super(SupervisorCreateForm, self).save(commit=False)
        user.is_supervisor = True
        user.is_employee = False
        user.save()

        Supervisor.objects.create(user=user)
        return user


class HrCreateForm(UserCreateForm):
    def save(self, commit=True):
        user = super(HrCreateForm, self).save(commit=False)
        user.is_hr = True
        user.is_employee = False

        user.save()
        Hr.objects.create(user=user)

        return user


class DivisionCreateForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = "__all__"
