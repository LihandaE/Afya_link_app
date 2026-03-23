from django.urls import path
from .views import (
    create_visit,
    nurse_queue,
    doctor_queue,
    record_vitals,
    doctor_consultation
)

urlpatterns = [

    # Receptionist creates visit
    path("create/", create_visit, name="create_visit"),

    # Nurse dashboard queue
    path("nurse-queue/", nurse_queue, name="nurse_queue"),

    # Doctor dashboard queue
    path("doctor-queue/", doctor_queue, name="doctor_queue"),

    # Nurse records vitals
    path("vitals/", record_vitals, name="record_vitals"),

    # Doctor consultation
    path("consultation/", doctor_consultation, name="doctor_consultation"),

]