from django.db import models

# Create your models here.

class LabTest(models.Model):
    STATUS_CHOICES=(
        ('requested', 'Requested'),
        ('completed', 'Completed'),
    )
    visit=models.ForeignKey(
        'visits.Visit',
        on_delete=models.CASCADE

    )
    doctor= models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='lab_requested_by'

    )
    lab_technician=models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lab_performed_by'
    )
    test_type=models.CharField(max_length=260)
    result=models.TextField(blank=True, null=True)

    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='requested'
    )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.test_type} - {self.visit.patient.full_name}"
    