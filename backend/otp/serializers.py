from rest_framework import serializers
from .models import OTPVerification

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model=OTPVerification
        fields='__all__'
        