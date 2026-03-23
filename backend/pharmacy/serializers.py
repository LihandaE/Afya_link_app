from .models import *
from rest_framework import serializers


class DispenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispenseMedication
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = "__all__"