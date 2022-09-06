# from django.urls import path, include

# from ..urls.routers import urlpatterns as pat
# from apps.views.API.basicAPIView import UtilityTypeAPIView, PropertyAPIView
from rest_framework.routers import SimpleRouter

from ..views.API.accountAPIView import UserViewSet
from apps.views.API.authViewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from apps.views.API.propertyViewset import PropertyViewSet
from apps.views.API.feeAPIView import UtilityTypeViewSet

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# PROPERTY
routes.register(r'property', PropertyViewSet, basename='property')

# Fee
routes.register(r'utilitytype', UtilityTypeViewSet, basename="utility-type")

urlpatterns = [
    *routes.urls,
    # path(r'property/<int:detailed>', PropertyAPIView.as_view(), name='properties'),
    # path(r'utility_types/<int:detailed>/', UtilityTypeAPIView.as_view(), name='utilities'),
]
