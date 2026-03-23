from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OTPVerification
from .utils import generate_otp
from patients.models import Patient
# Create your views here.

@api_view(['POST'])
def send_otp(request):
    patient_id=request.data.get('patient_id')
    patient=Patient.objects.get(id=patient_id)
    otp_code=generate_otp()

    OTPVerification.objects.create(
        patient=patient,
        otp_code=otp_code,
        purpose='record_access'
    )

    print('OTP:', otp_code)
    return Response({
        'message': 'OTP sent to patient'
    })

@api_view(['POST'])
def verify_otp(request):
    patient_id=request.data.get('patient_id')
    otp_input=request.data.get('otp')
    otp=OTPVerification.objects.filter(
        patient_id=patient_id,
        otp_code=otp_input,
        is_verified=False

    ).first()

    if not otp:
        return Response(
            {
                'error':'Invalid OTP'
            }
        )
    otp.is_verified=True
    otp.save()
    return Response({
        'message': 'OTP verified. Access granted'
    })
