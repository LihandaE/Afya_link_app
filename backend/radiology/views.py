from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import RadiologyReport
from .serializers import RadiologySerializer
from accounts.permissions import IsDoctor, IsRadiologist
from visits.models import Visit



# 1. RADIOLOGY QUEUE (Radiologist)

@api_view(["GET"])
@permission_classes([IsRadiologist])
def radiology_queue(request):
    """
    Returns all pending radiology scans.
    Only Radiologists can access.
    """

    scans = RadiologyReport.objects.filter(
        result__isnull=True
    ).select_related("visit", "doctor")

    serializer = RadiologySerializer(scans, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)



# 2. REQUEST SCAN (Doctor)


@api_view(["POST"])
@permission_classes([IsDoctor])
def request_scan(request):
    """
    Doctor requests a radiology scan for a visit.
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
            {"error": "Radiology can only be requested after doctor consultation"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = RadiologySerializer(data=request.data)

    if serializer.is_valid():

        scan = serializer.save(
            doctor=request.user
        )

        # Update visit status
        visit.status = "radiology_requested"
        visit.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3. UPLOAD SCAN RESULT (Radiologist)


@api_view(["POST"])
@permission_classes([IsRadiologist])
def upload_scan_result(request):
    """
    Radiologist uploads scan results and image.
    """

    scan_id = request.data.get("id")

    # Validate scan
    try:
        scan = RadiologyReport.objects.get(id=scan_id)
    except RadiologyReport.DoesNotExist:
        return Response(
            {"error": "Radiology report not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    # Prevent duplicate uploads
    if scan.result:
        return Response(
            {"error": "Scan result already uploaded"},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = RadiologySerializer(scan, data=request.data, partial=True)

    if serializer.is_valid():

        updated_scan = serializer.save(
            radiologist=request.user
        )

        # Send patient back to doctor
        visit = updated_scan.visit
        visit.status = "doctor_consult"
        visit.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)