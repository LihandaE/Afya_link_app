from rest_framework import serializers
from .models import RadiologyReport


class RadiologySerializer(serializers.ModelSerializer):

    class Meta:
        model = RadiologyReport
        fields = "__all__"