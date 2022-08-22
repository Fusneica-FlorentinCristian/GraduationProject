from django.urls import path, include
from ..urls.routers import urlpatterns as pat
from apps.views.API.basicAPIView import UtilityTypeAPIView, PropertyAPIView

urlpatterns = [
    path('', include(('apps.urls.routers', 'apps'), namespace='core-api')),
    path(r'property/<int:detailed>', PropertyAPIView.as_view(), name='properties'),
    path(r'utility_types/<int:detailed>/', UtilityTypeAPIView.as_view(), name='utilities'),
]
