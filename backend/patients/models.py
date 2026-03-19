from django.db import models

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES=(
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    full_name=models.CharField(max_length=280)
    phone=models.CharField(max_length=25)
    email=models.EmailField(blank=True, null=True)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    national_id=models.CharField(max_length=50, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name