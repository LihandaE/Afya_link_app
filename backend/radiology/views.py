from django.shortcuts import render
from accounts.permissions import IsRadiologist
from rest_framework.decorators import*
from rest_framework.response import Response
from .serializers import RadiologySerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsRadiologist])
def upload_radiology(request):
    serializer=RadiologySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(radiologist=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)
