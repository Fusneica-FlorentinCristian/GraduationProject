from ..models import Property, Country, Region, City
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        read_only_field = '__all__'


class CountryReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        read_only_field = '__all__'


class RegionReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        read_only_field = '__all__'


class CityReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        read_only_field = '__all__'
