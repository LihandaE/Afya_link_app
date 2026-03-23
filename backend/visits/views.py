from django.shortcuts import render
from accounts.permissions import *
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
        visit=serializer.validated_data['visit']
        visit.status='vitals_done'
        visit.save()
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

@api_view(['POST'])
@permission_classes([IsReceptionist])
def create_visit(request):
    serializer=VisitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(receptionist=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["GET"])
def nurse_queue(request):

    visits = Visit.objects.filter(status="registered")

    serializer = VisitSerializer(visits, many=True)

    return Response(serializer.data)