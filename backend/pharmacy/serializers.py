from .models import *
from rest_framework import serializers


class DispenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispenseMedication
        fields = "__all__"