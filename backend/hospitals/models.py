from django.db import models

# Create your models here.

class Hospital(models.Model):
    name=models.CharField(max_length=300)
    location=models.CharField(max_length=280)
    services=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    