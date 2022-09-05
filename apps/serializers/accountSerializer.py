# from rest_auth.serializers import UserDetailsSerializer

from apps.models.modelsAccount import User, Tenant, Administrator
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', "isAdministrator", "isTenant"]
        read_only_field = ['is_active']
    #
    # def __dict__(self):
    #     return dict(self)


class TenantsReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        read_only_field = ["countryInterested", "regionInterested", "cityInterested", "user"]

    # def __dict__(self):


class AdministratorReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        read_only_field = ["isCollaborator", "user"]


class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_field = ["first_name", "last_name", "username", "phone_number"]
