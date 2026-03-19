from django.db import models

# Create your models here.

class Prescription(models.Model) :
    visit=models.ForeignKey(
        'visits.Visit',
        on_delete=models.CASCADE

    )
    doctor=models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True
    )
    medication=models.CharField(max_length=255)
    dosage=models.CharField(max_length=260)
    instructions=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.visit.patient.full_name}"


#Pharmacy Dispensing
    
class DispenseMedication(models.Model):
    prescription=models.OneToOneField(
        Prescription,
        on_delete=models.CASCADE

    )
    pharmacist=models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True
    )
    dispensed_at=models.DateTimeField(auto_now_add=True)

    status=models.CharField(
        max_length=50,
        default='dispensed'

    )
    def __str__(self):
        return f"Dispensed for{self.prescription.visit.patient.full_name}"