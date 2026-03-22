from django.shortcuts import render
from accounts.permissions import IsNurse, IsDoctor
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
# Create your views here.

@api_view(['POST'])
@permission_classes({IsNurse})
def record_vitals(request):
    serializer=VitalsSerializer(data=request.data)
    if serializer.is_valid:
        serializer.save(nurse=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([IsDoctor])
def doctor_consultation(request):
    serializer= MedicalRecordSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(doctor=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)