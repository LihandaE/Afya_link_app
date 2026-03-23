from django.urls import path
from .views import (
    pharmacy_queue,create_prescription,dispense_medication)

urlpatterns = [

    # Pharmacy queue
    path("queue/", pharmacy_queue, name="pharmacy_queue"),

    # Doctor creates prescription
    path("prescribe/", create_prescription, name="create_prescription"),

    # Pharmacist dispenses medication
    path("dispense/", dispense_medication, name="dispense_medication"),

]