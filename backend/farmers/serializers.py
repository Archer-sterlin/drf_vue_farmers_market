from rest_framework import serializers

from auth_api.models import User
from product.models import Category
from farmers.models import Farmer


class RegisterFarmerSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    location = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.IntegerField(required=True, write_only=True)
    farming_type = serializers.CharField(required=True, write_only=True)
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "location",
            "farming_type",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        try:
            password = validated_data.pop("password", None)
            new_user = self.Meta.model(
                email=validated_data["email"], username=validated_data["username"], is_farmer=True
            )
            if password is not None:
                new_user.set_password(password)

            new_user.save()

            new_farmer = Farmer(
                user=new_user,
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                phone_number=validated_data["phone_number"],
                location=validated_data["location"],
                farming_type=validated_data["farming_type"],
            )
            
            category = Category(
                name=validated_data["farming_type"],
                slug=validated_data["farming_type"].replace(" ","_")
                )
            category.save()
            new_farmer.save()

            return new_user

        except Exception as error:
            return error
