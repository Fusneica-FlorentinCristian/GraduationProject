from rest_framework import serializers
from ..models import UtilityType


class UtilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilityType
        fields = '__all__'
