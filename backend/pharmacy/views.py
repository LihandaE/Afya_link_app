from django.shortcuts import render
from accounts.permissions import IsPharmacist
from rest_framework.decorators import *
from rest_framework.response import Response
from .serializers import DispenseSerializer


# Create your views here.

@api_view(['POST'])
@permission_classes([IsPharmacist])
def dispense_drug(request):
    serializer=DispenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(pharmacist=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)