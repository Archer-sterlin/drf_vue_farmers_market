from django.conf import settings
from django.db import models


# Create your models here.
class Farmer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    farming_type = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

