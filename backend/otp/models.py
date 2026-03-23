from django.db import models

# Create your models here.
class OTPVerification(models.Model):
    PURPOSE_CHOICES=(
        ('record_access', 'Record Access'),
        ('login_verification', 'Login Verification'),

    )
    patient=models.ForeignKey(
        'patients.Patient', on_delete=models.CASCADE

    )
    otp_code= models.CharField(max_length=7)
    purpose=models.CharField(
        max_length=60,
        choices=PURPOSE_CHOICES
    )
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.patient.full_name}"
    