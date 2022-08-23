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


#
# class Crop(models.Model):
#     farmer = models.ForeignKey(Farmer, related_name="farmer", on_delete=models.CASCADE)
#     crop_name = models.CharField(max_length=200)
#     quantity = models.IntegerField(default=0)
#     price = models.FloatField(default=0.00)
#     delivery_type = models.CharField(max_length=200)
#     discount = models.FloatField(default=0.00)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.crop_name}"
#
#     class Meta:
#         ordering = ('-created_at',)
