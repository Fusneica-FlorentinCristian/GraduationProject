from django.core.exceptions import ObjectDoesNotExist

from ..models import Property, Country, Region, City
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        try:
            estate = Property.objects.get(pk=validated_data['id'])
        except ObjectDoesNotExist:
            try:
                estate = Property.objects.create_user(**validated_data)
            except Exception as e:
                raise e
        return estate

    def save(self, owner, validated_data):
        try:
            property = Property.objects.create_property(owner_user_id=owner, **validated_data)
        except Exception as e:
            raise e
        return property

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
