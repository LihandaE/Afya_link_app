from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .models import *
from visits.models import Visit
from laboratory.models import LabTest
from radiology.models import RadiologyReport
from pharmacy.models import Prescription
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

@api_view(['GET'])
def patient_history(request, patient_id):
    visits=Visit.objects.filter(patient_id=patient_id)
    labs=LabTest.objects.filter(visit__patient_id=patient_id)
    scans=RadiologyReport.objects.filter(visit__patient_id=patient_id)
    prescriptions=Prescription.objects.filter(visit__patient_id=patient_id)

    data={
        'visits':visits.values(),
        'lab_results':labs.values(),
        'radiology':scans.values(),
        'prescriptions':prescriptions.values()
    }

    return Response(data)

