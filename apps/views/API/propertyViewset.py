from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.response import Response

from ...models import Property
from ...serializers.propertySerializer import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class PropertyViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = PropertySerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # , filters.OrderingFilter]
    filterset_fields = ["id", 'location', 'owner', "usable_area", "currency_type", "rent_price", "selling_price"]
    search_fields = ["id", 'location', 'owner', "usable_area", "currency_type", "rent_price", "selling_price"]
    ordering_fields = ["id", 'location', 'owner', "usable_area", "currency_type", "rent_price", "selling_price"]
    ordering = ['id', 'usable_area']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # if self.request.user.is_superuser:
        return self.serializer_class.Meta.model.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = Property.objects.get(lookup_field_value)
        return obj

    def retrieve(self, request, pk=None):
        queryset = Property.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PropertySerializer(user)
        return Response(serializer.data)
