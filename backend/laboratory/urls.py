from django.urls import path
from .views import (lab_queue,request_lab_test,upload_lab_result)

urlpatterns = [

    # Lab technician queue
    path("queue/", lab_queue, name="lab_queue"),

    # Doctor requests lab test
    path("request/", request_lab_test, name="request_lab_test"),

    # Lab technician uploads result
    path("result/", upload_lab_result, name="upload_lab_result"),

]