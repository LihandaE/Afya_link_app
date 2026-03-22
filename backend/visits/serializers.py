from .models import Vitals, MedicalRecord
from rest_framework import serializers


class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vitals
        fields='__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalRecord
        fields='__all__'
        