from django.db import models

# Create your models here.
from django.db import models

# visit model
class Visit(models.Model):

    STATUS_CHOICES = (

        ('registered', 'Registered'),
        ('vitals_done', 'Vitals Done'),
        ('doctor_consult', 'Doctor Consultation'),
        ('lab_requested', 'Lab Requested'),
        ('radiology_requested', 'Radiology Requested'),
        ('diagnosed', 'Diagnosed'),
        ('pharmacy', 'Pharmacy'),
        ('completed', 'Completed'),

    )

    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE
    )

    hospital = models.ForeignKey(
        'hospitals.Hospital',
        on_delete=models.CASCADE
    )

    receptionist = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='registered'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit {self.id} - {self.patient.full_name}"
    
#vitals model for the nurse
class Vitals(models.Model):
    visit=models.OneToOneField(
        'Visit',
        on_delete=models.CASCADE

    )
    nurse=models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True
    )
    temperature=models.FloatField()
    blood_pressure=models.CharField(max_length=20)
    weight=models.FloatField()
    heart_rate=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vitals for{self.visit.patient.full_name}"

#Medical Records model

class MedicalRecord(models.Model):
    visit=models.ForeignKey(
        Visit,
        on_delete=models.CASCADE
    )

    doctor=models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True
    )
    symptoms=models.TextField()
    diagnosis=models.TextField(blank=True, null=True)
    notes=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.visit.patient.full_name}"