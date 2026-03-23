from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import LabTest
from .serializers import LabTestSerializer

from accounts.permissions import IsDoctor, IsLabTech
from visits.models import Visit


# 1. LAB QUEUE (Lab Technician)

@api_view(["GET"])
@permission_classes([IsLabTech])
def lab_queue(request):
    """
    Returns all pending lab tests.
    Only Lab Technicians can access.
    """

    tests = LabTest.objects.filter(status="requested").select_related("visit", "doctor")

    serializer = LabTestSerializer(tests, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


# 2. REQUEST LAB TEST (Doctor)


@api_view(["POST"])
@permission_classes([IsDoctor])
def request_lab_test(request):
    """
    Doctor requests a lab test for a patient visit.
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

    # Optional: enforce workflow (only after consultation)
    if visit.status not in ["doctor_consult"]:
        return Response(
            {"error": "Lab can only be requested after doctor consultation"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = LabTestSerializer(data=request.data)

    if serializer.is_valid():

        lab_test = serializer.save(
            doctor=request.user,
            status="requested"
        )

        # Update visit status
        visit.status = "lab_requested"
        visit.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 3. UPLOAD LAB RESULT (Lab Technician)


@api_view(["POST"])
@permission_classes([IsLabTech])
def upload_lab_result(request):
    """
    Lab technician uploads lab results.
    """

    test_id = request.data.get("id")

    # Validate test
    try:
        lab_test = LabTest.objects.get(id=test_id)
    except LabTest.DoesNotExist:
        return Response(
            {"error": "Lab test not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Prevent overwriting completed tests
    if lab_test.status == "completed":
        return Response(
            {"error": "Lab result already uploaded"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = LabTestSerializer(lab_test, data=request.data, partial=True)

    if serializer.is_valid():

        updated_test = serializer.save(
            lab_technician=request.user,
            status="completed"
        )

        # After lab, return patient to doctor
        visit = updated_test.visit
        visit.status = "doctor_consult"
        visit.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)