from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from .models import OTPVerification
from .utils import generate_otp
from .sms import send_sms

from patients.models import Patient


# 1. SEND OTP

@api_view(["POST"])
def send_otp(request):
    """
    Sends OTP to patient phone.
    Includes rate limiting and expiration.
    """

    patient_id = request.data.get("patient_id")

    # Validate patient
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response(
            {"error": "Patient not found"},
            status=status.HTTP_404_NOT_FOUND
        )

   
    # RATE LIMITING (max 3 per minute)
   

    one_minute_ago = timezone.now() - timedelta(minutes=1)

    recent_otps = OTPVerification.objects.filter(
        patient=patient,
        created_at__gte=one_minute_ago
    ).count()

    if recent_otps >= 3:
        return Response(
            {"error": "Too many OTP requests. Try again later."},
            status=status.HTTP_429_TOO_MANY_REQUESTS
        )

   
    # GENERATE OTP
    

    otp_code = generate_otp()

   
    # SAVE OTP WITH EXPIRY (3 min)
   

    otp = OTPVerification.objects.create(
        patient=patient,
        otp_code=otp_code,
        purpose="record_access",
        expires_at=timezone.now() + timedelta(minutes=3)
    )

    
    # SEND SMS (Africa's Talking)
 

    message = f"Your AfyaLink OTP is {otp_code}. It expires in 3 minutes."

    # Ensure phone format is international (+254...)
    send_sms(patient.phone, message)

    return Response({
        "message": "OTP sent successfully"
    }, status=status.HTTP_200_OK)



# 2. VERIFY OTP


@api_view(["POST"])
def verify_otp(request):
    """
    Verifies OTP and grants access.
    """

    patient_id = request.data.get("patient_id")
    otp_input = request.data.get("otp")

    otp = OTPVerification.objects.filter(
        patient_id=patient_id,
        otp_code=otp_input,
        is_verified=False
    ).first()

    if not otp:
        return Response(
            {"error": "Invalid OTP"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # CHECK EXPIRY
   
    if otp.is_expired():
        return Response(
            {"error": "OTP expired"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # MARK AS VERIFIED (ONE-TIME USE)

    otp.is_verified = True
    otp.save()

    return Response({
        "message": "OTP verified. Access granted."
    }, status=status.HTTP_200_OK)