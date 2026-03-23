from django.urls import path
from .views import (register_patient,search_patient,patient_history)

urlpatterns = [

    # Register patient (Receptionist)
    path("register/", register_patient, name="register_patient"),

    # Search patient (Receptionist, Doctor)
    path("search/", search_patient, name="search_patient"),

    # Patient full medical history (OTP protected)
    path("history/<int:patient_id>/", patient_history, name="patient_history"),

]