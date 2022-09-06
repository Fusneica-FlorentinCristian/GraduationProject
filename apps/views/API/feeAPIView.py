from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters

from ...models import UtilityType
from ...models.modelsAccount import User
from ...serializers.feeSerializer import UtilityTypeSerializer


class UtilityTypeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UtilityTypeSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UtilityType.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = UtilityType.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
