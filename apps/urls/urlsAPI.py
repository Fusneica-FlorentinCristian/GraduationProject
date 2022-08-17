from django.urls import path

from apps.views.viewsAPI import UtilityTypeAPIView, PropertyAPIView

urlpatterns = [
    path('property/<int:detailed>', PropertyAPIView.as_view(), name='properties'),
    path('utility_types/<int:detailed>/', UtilityTypeAPIView.as_view(), name='utilities'),
]