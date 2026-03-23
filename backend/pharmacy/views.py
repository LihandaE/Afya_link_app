from django.shortcuts import render
from accounts.permissions import *
from rest_framework.decorators import *
from rest_framework.response import Response
from .serializers import *


# Create your views here.

@api_view(["POST"])
@permission_classes([IsPharmacist])
def dispense_medication(request):

    serializer = DispenseSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save(pharmacist=request.user)

        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(["POST"])
@permission_classes([IsDoctor])
def create_prescription(request):

    serializer = PrescriptionSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save(doctor=request.user)

        return Response(serializer.data)

    return Response(serializer.errors)