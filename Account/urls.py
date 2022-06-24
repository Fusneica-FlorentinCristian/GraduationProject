from django.urls import include, path


urlpatterns = [
    # path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]