from .models import Vitals
from rest_framework import serializers


class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vitals
        fields='__all__'