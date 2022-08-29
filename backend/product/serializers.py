from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "farmer",
            "product_name",
            "get_absolute_url",
            "category",
            "quantity",
            "price",
            "delivery_type",
            "discount",
            "get_image",
            "get_thumbnail"
        )
        read_only_fields = ("farmer", "id")


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "products",
        )
