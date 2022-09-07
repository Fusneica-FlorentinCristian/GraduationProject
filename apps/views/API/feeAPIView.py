from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.response import Response

from ...models import UtilityType
from ...models.modelsAccount import User
from ...serializers.accountSerializer import UserSerializer
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

    def list(self, request):
        queryset = UtilityType.objects.all()
        serializer = UtilityTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        ut = get_object_or_404(queryset, pk=pk)
        serializer = UtilityTypeSerializer(ut)
        return Response(serializer.data)

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = UtilityType.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
