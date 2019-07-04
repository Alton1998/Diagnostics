from rest_framework import serializers
from . models import Fertility

class FertilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Fertility
        fields=('__all__')