from django.urls import path
from GraduationProject.views import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name="profile"),
    path('profile/<str:username>/', views.profile, name="profile"),
    # path('profile', views.profile, name='profile'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
