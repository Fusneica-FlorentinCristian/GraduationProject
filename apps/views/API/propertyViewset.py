from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters

from ...models import Property
from ...serializers.propertySerializer import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = PropertySerializer
    permission_classes = (AllowAny,)
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['updated']
    # ordering = ['-updated']

    def get_queryset(self):
        # if self.request.user.is_superuser:
        return Property.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = Property.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
