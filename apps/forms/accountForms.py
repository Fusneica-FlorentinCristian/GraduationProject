from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

# from classroom.models import (Answer, Question, Student, StudentAnswer,
#                               Subject, User)

from apps.models.modelsAccount import Tenant, User
from apps.models.modelsProperty import Country


class AdministratorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.isAdministrator = True
        if commit:
            user.save()
        return user


class TenantSignUpForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(TenantSignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['interest_country'].choices = countries

    interest_countries = forms.ModelMultipleChoiceField(
        queryset=Country.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Countries interested in"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + tuple(['interest_countries'])

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.isTenant = True
        user.save()
        Tenant.objects.create(user=user)
        return user


class TenantInterestsForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('countryInterested',)
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }
