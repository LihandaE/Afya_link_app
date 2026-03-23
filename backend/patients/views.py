from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Patient
from .serializers import PatientSerializer

from accounts.permissions import IsReceptionist
from visits.models import Visit, Vitals, MedicalRecord
from laboratory.models import LabTest
from radiology.models import RadiologyReport
from pharmacy.models import Prescription
from otp.models import OTPVerification



# 1. REGISTER PATIENT (Receptionist)


@api_view(["POST"])
@permission_classes([IsReceptionist])
def register_patient(request):
    """
    Registers a new patient.
    Only Receptionists can perform this action.
    """

    national_id = request.data.get("national_id")

    # Prevent duplicate patients
    if Patient.objects.filter(national_id=national_id).exists():
        return Response(
            {"error": "Patient already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 2. SEARCH PATIENT


@api_view(["GET"])
def search_patient(request):
    """
    Search patient by phone or national ID.
    Accessible to authenticated staff.
    """

    phone = request.GET.get("phone")
    national_id = request.GET.get("national_id")

    queryset = Patient.objects.all()

    if phone:
        queryset = queryset.filter(phone__icontains=phone)

    if national_id:
        queryset = queryset.filter(national_id__icontains=national_id)

    serializer = PatientSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)



# 3. PATIENT HISTORY (OTP PROTECTED)


@api_view(["GET"])
def patient_history(request, patient_id):
    """
    Returns full patient medical history.
    Requires OTP verification for security.
    """

    # Check patient exists
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response(
            {"error": "Patient not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # OTP verification check
    otp_verified = OTPVerification.objects.filter(
        patient=patient,
        is_verified=True
    ).exists()

    if not otp_verified:
        return Response(
            {"error": "OTP verification required"},
            status=status.HTTP_403_FORBIDDEN
        )

    # Fetch all related data
    visits = Visit.objects.filter(patient=patient)
    vitals = Vitals.objects.filter(visit__patient=patient)
    records = MedicalRecord.objects.filter(visit__patient=patient)
    labs = LabTest.objects.filter(visit__patient=patient)
    scans = RadiologyReport.objects.filter(visit__patient=patient)
    prescriptions = Prescription.objects.filter(visit__patient=patient)

    data = {

        "patient": PatientSerializer(patient).data,

        "visits": list(visits.values()),

        "vitals": list(vitals.values()),

        "medical_records": list(records.values()),

        "lab_results": list(labs.values()),

        "radiology_reports": list(scans.values()),

        "prescriptions": list(prescriptions.values()),

    }

    return Response(data, status=status.HTTP_200_OK)