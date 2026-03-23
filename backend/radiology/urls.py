from django.urls import path
from .views import (
    radiology_queue,request_scan,upload_scan_result
)

urlpatterns = [

    # Radiology queue
    path("queue/", radiology_queue, name="radiology_queue"),

    # Doctor requests scan
    path("request/", request_scan, name="request_scan"),

    # Radiologist uploads result
    path("result/", upload_scan_result, name="upload_scan_result"),

]