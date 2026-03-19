from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    ROLE_CHOICES=(
        ('super_admin','Super Admin'),
        ('hospital_admin','Hospital Admin'),
        ('doctor','Doctor'),
        ('nurse','Nurse'),
        ('receptionist','Receptionist'),
        ('pharmacist','Pharmacist'),
        ('lab_tech','Lab Technician'),
        ('radiologist','Radiologist'),
        ('patient','Patient'),
    )
    role= models.CharField(max_length=30, choices=ROLE_CHOICES)
    phone=models.CharField(max_length=20)
    license_number = models.CharField(max_length=100, blank=True, null=True)

    profile_image =models.CloudinaryField(upload_to='staff_images/', blank=True, null=True)

    hospital = models.ForeignKey(
        'hospitals.Hospital',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):

        return self.username