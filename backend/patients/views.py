from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .models import Patient
from  accounts.permissions import IsReceptionist
from .serializers import PatientSerializer
from rest_framework.response import Response

# Create your views here.

@api_view({'POST'})
@permission_classes({IsReceptionist})
def register_patient(request):
    serializer= PatientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["GET"])
def search_patient(request):
    phone=request.GET.get('phone')
    patient=Patient.objects.filter(phone=phone)
    serializer=PatientSerializer(patient, many=True)
    return Response(serializer.data)


