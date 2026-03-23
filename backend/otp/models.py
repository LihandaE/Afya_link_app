from django.db import models
from django.utils import timezone
from datetime import timedelta

# DEFAULT EXPIRY FUNCTION (IMPORTANT)

def default_expiry():
    """
    Returns expiry time 5 minutes from now.
    This ensures each OTP gets its own correct expiry.
    """
    return timezone.now() + timedelta(minutes=5)


# OTP MODEL

class OTPVerification(models.Model):

    PURPOSE_CHOICES = (
        ('record_access', 'Record Access'),
    )

    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE,
        related_name='otps'
    )

    otp_code = models.CharField(max_length=6)

    purpose = models.CharField(
        max_length=50,
        choices=PURPOSE_CHOICES,
        default='record_access'
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    expires_at = models.DateTimeField(default=default_expiry)


    # HELPER METHODS

    def is_expired(self):
        """
        Check if OTP is expired.
        """
        return timezone.now() > self.expires_at

    def __str__(self):
        return f"OTP for {self.patient.full_name} ({self.otp_code})"