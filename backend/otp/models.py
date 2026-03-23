from django.db import models
from django.utils import timezone


class OTPVerification(models.Model):

    PURPOSE_CHOICES = (
        ('record_access', 'Record Access'),
    )

    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE
    )

    otp_code = models.CharField(max_length=6)

    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"OTP for {self.patient.full_name}"