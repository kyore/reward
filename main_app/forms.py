from django import forms
from django.forms import formset_factory

from main_app.models import OwnRating, Rating, HRRating


class OwnRatingForm(forms.ModelForm):
    month = forms.DateField(label="Сар", input_formats=['%Y-%m'])

    class Meta:
        model = OwnRating
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['month'].widget.attrs = {'class': 'months', 'autocomplete': 'new-password'}


OwnRatingFormSet = formset_factory(OwnRatingForm)


# Supervisor Rating Form *********************************


class SupervisorRatingCreateForm(forms.ModelForm):
    month = forms.DateField(label="Сар", input_formats=['%Y-%m'])

    class Meta:
        model = Rating
        exclude = ('supervisor',)

    def __init__(self, *args, **kwargs):
        super(SupervisorRatingCreateForm, self).__init__(*args, **kwargs)
        self.fields['month'].widget.attrs = {'class': 'months', 'autocomplete': 'new-password'}


SupervisorRatingCreateFormSet = formset_factory(SupervisorRatingCreateForm)


# HR Rating Form *********************************

class HrRatingCreateForm(forms.ModelForm):
    month = forms.DateField(label="Сар", input_formats=['%Y-%m'])

    class Meta:
        model = HRRating
        exclude = ('hr',)

    def __init__(self, *args, **kwargs):
        super(HrRatingCreateForm, self).__init__(*args, **kwargs)
        self.fields['month'].widget.attrs = {'class': 'months', 'autocomplete': 'new-password'}


HrRatingCreateFormSet = formset_factory(HrRatingCreateForm)
