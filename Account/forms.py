from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

# from classroom.models import (Answer, Question, Student, StudentAnswer,
#                               Subject, User)

from Account.models import Tenant, Administrator, User, Enterprise
from Property.models import Country


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


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ('name',)


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')

# class TakeQuizForm(forms.ModelForm):
#     answer = forms.ModelChoiceField(
#         queryset=Answer.objects.none(),
#         widget=forms.RadioSelect(),
#         required=True,
#         empty_label=None)
#
#     class Meta:
#         model = StudentAnswer
#         fields = ('answer', )
#
#     def __init__(self, *args, **kwargs):
#         question = kwargs.pop('question')
#         super().__init__(*args, **kwargs)
#         self.fields['answer'].queryset = question.answers.order_by('text')
