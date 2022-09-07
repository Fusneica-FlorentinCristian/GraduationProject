from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.response import Response

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
        return obj

    def list(self, request):
        queryset = Property.objects.all()
        serializer = PropertySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Property.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PropertySerializer(user)
        return Response(serializer.data)
