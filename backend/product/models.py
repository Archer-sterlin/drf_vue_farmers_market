from django.db import models

from farmers.models import Farmer


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    farmer = models.ForeignKey(Farmer, related_name="farmer", on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.00)
    delivery_type = models.CharField(max_length=200)
    discount = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.crop_name
