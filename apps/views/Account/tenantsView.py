from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from apps.forms.accountForms import TenantSignUpForm  # , TakeQuizForm
from apps.models.modelsAccount import Tenant


class TenantSignUpView(CreateView):
    model = Tenant
    form_class = TenantSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'tenant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
