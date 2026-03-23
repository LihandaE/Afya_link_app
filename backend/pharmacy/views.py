from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Prescription, DispenseMedication
from .serializers import PrescriptionSerializer, DispenseSerializer

from accounts.permissions import IsDoctor, IsPharmacist
from visits.models import Visit



# 1. PHARMACY QUEUE (Pharmacist)


@api_view(["GET"])
@permission_classes([IsPharmacist])
def pharmacy_queue(request):
    """
    Returns all prescriptions that have NOT been dispensed.
    """

    prescriptions = Prescription.objects.filter(
        dispensedmedication__isnull=True
    ).select_related("visit", "doctor")

    serializer = PrescriptionSerializer(prescriptions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


# 2. CREATE PRESCRIPTION (Doctor)


@api_view(["POST"])
@permission_classes([IsDoctor])
def create_prescription(request):
    """
    Doctor creates prescription for a patient visit.
    """

    visit_id = request.data.get("visit")

    # Validate visit
    try:
        visit = Visit.objects.get(id=visit_id)
    except Visit.DoesNotExist:
        return Response(
            {"error": "Visit not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Enforce workflow
    if visit.status not in ["doctor_consult"]:
        return Response(
            {"error": "Prescription can only be created after consultation"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = PrescriptionSerializer(data=request.data)

    if serializer.is_valid():

        prescription = serializer.save(
            doctor=request.user
        )

        # Move patient to pharmacy stage
        visit.status = "pharmacy"
        visit.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 3. DISPENSE MEDICATION (Pharmacist)


@api_view(["POST"])
@permission_classes([IsPharmacist])
def dispense_medication(request):
    """
    Pharmacist dispenses medication.
    Marks visit as COMPLETED.
    """

    prescription_id = request.data.get("prescription")

    # Validate prescription
    try:
        prescription = Prescription.objects.get(id=prescription_id)
    except Prescription.DoesNotExist:
        return Response(
            {"error": "Prescription not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Prevent double dispensing
    if hasattr(prescription, "dispensedmedication"):
        return Response(
            {"error": "Medication already dispensed"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = DispenseSerializer(data=request.data)

    if serializer.is_valid():

        dispense = serializer.save(
            pharmacist=request.user,
            prescription=prescription
        )

        # Mark visit as completed
        visit = prescription.visit
        visit.status = "completed"
        visit.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)