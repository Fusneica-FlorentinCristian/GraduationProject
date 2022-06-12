from django.urls import path
from utility_bills import views


urlpatterns = [
    path('', views.index, name='index')
]