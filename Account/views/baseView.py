from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from Account.models import User


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    # if request.user.is_authenticated:
    #     if request.user.isAdministrator:
    #         return render(request, 'Account/home.html')
    #     else:
    #         return render(request, 'Account/home.html')
    return render(request, 'Account/home.html')


def profile(request, username=None):
    if username and (not request.user.is_authenticated or username is not request.user.username):
        user_profile = User.objects.filter(username=username).first()
    elif request.user.is_authenticated:
        user_profile = request.user
    else:
        return redirect('home')

    if user_profile:
        return render(request, "Account/profile.html", context={"user_profile": user_profile})
    else:
        return render(request, "404.html", context={"message": "User not found"})
