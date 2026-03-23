from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Visit, Vitals, MedicalRecord
from .serializers import VisitSerializer, VitalsSerializer, MedicalRecordSerializer

from accounts.permissions import IsReceptionist, IsNurse, IsDoctor
from patients.models import Patient
from hospitals.models import Hospital


# 1. CREATE VISIT (Receptionist)

@api_view(["POST"])
@permission_classes([IsReceptionist])
def create_visit(request):
    """
    Creates a new hospital visit when a patient arrives.
    Only Receptionists are allowed.
    """

    patient_id = request.data.get("patient")
    hospital_id = request.data.get("hospital")

    # Validate patient
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return Response(
            {"error": "Patient not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Validate hospital
    try:
        hospital = Hospital.objects.get(id=hospital_id)
    except Hospital.DoesNotExist:
        return Response(
            {"error": "Hospital not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    visit = Visit.objects.create(
        patient=patient,
        hospital=hospital,
        receptionist=request.user,
        status="registered"
    )

    serializer = VisitSerializer(visit)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 2. NURSE QUEUE


@api_view(["GET"])
@permission_classes([IsNurse])
def nurse_queue(request):
    """
    Returns all patients waiting for vitals.
    Status = registered
    """

    visits = Visit.objects.filter(status="registered").select_related("patient")

    serializer = VisitSerializer(visits, many=True)

    return Response(serializer.data)



# 3. DOCTOR QUEUE


@api_view(["GET"])
@permission_classes([IsDoctor])
def doctor_queue(request):
    """
    Returns patients ready for doctor consultation.
    Status = vitals_done
    """

    visits = Visit.objects.filter(status="vitals_done").select_related("patient")

    serializer = VisitSerializer(visits, many=True)

    return Response(serializer.data)



# 4. RECORD VITALS (Nurse)


@api_view(["POST"])
@permission_classes([IsNurse])
def record_vitals(request):
    """
    Nurse records patient vitals.
    Automatically updates visit status → vitals_done
    """

    serializer = VitalsSerializer(data=request.data)

    if serializer.is_valid():

        # Save vitals with nurse
        vitals = serializer.save(nurse=request.user)

        # Update visit status
        visit = vitals.visit
        visit.status = "vitals_done"
        visit.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 5. DOCTOR CONSULTATION


@api_view(["POST"])
@permission_classes([IsDoctor])
def doctor_consultation(request):
    """
    Doctor records consultation (symptoms, diagnosis).
    Updates visit status → doctor_consult
    """

    serializer = MedicalRecordSerializer(data=request.data)

    if serializer.is_valid():

        record = serializer.save(doctor=request.user)

        # Update visit status
        visit = record.visit
        visit.status = "doctor_consult"
        visit.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)