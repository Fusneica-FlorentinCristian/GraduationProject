from django.urls import include, path
from Account.views import baseView

urlpatterns = [
    path('', baseView.home, name='home'),
    path('profile/', baseView.profile, name="profile"),
    path('profile/<str:username>/', baseView.profile, name="profile"),
    # path('profile', views.profile, name='profile'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
