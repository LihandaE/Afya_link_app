from django.shortcuts import render
from accounts.permissions import IsLabTech
from rest_framework.decorators import *
from rest_framework.response import Response
from .serializers import LabTestSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsLabTech])
def upload_lab_result(request):
    serializer=LabTestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(lab_technician=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)
