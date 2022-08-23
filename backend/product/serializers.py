from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "farmer",
            "crop_name",
            "category",
            "quantity",
            "price",
            "delivery_type",
            "discount",
        )
        read_only_fields = ("farmer", "category")


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
