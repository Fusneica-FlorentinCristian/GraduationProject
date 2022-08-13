from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import (CreateView)

from apps.forms.accountForms import AdministratorSignUpForm
from apps.models.modelsAccount import User


class AdministratorSignUpView(CreateView):
    model = User
    form_class = AdministratorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('managers:quiz_change_list')
