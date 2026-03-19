from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class RadiologyReport(models.Model):
    visit=models.ForeignKey(
        'visits.Visit',
        on_delete=models.CASCADE

    )
    doctor=models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='radiology_requested_by'

    )
    radiologist=models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='radiology_done_by'

    )
    scan_type=models.CharField(max_length=260)
    result=models.TextField(blank=True, null=True)

    image=CloudinaryField(
        'images',
        blank=True,
        null=True
    )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.scan_type} -{self.visit.patient.full_name}"
    