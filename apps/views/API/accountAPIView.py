from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.response import Response

from ...models.modelsAccount import User
from ...serializers.accountSerializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # , filters.OrderingFilter]
    ordering_fields = ['username', "first_name", "last_name", "isAdministrator", "isTenant"]
    filterset_fields = ['username', "first_name", "last_name", "isAdministrator", "isTenant"]
    search_fields = ['username', "first_name", "last_name", "isAdministrator", "isTenant"]
    ordering = ['username']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # if self.request.user.is_superuser:
        return User.objects.all()

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
