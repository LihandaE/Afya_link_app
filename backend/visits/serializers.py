from .models import*
from rest_framework import serializers


class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vitals
        fields='__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalRecord
        fields='__all__'
        
class VisitSerializer(serializers.ModelsSerializer):
    class Meta:
        model=Visit
        fields='__all__'
