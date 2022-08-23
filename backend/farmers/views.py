from .serializers import FarmerSerializer, RegisterFarmerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Farmer
from auth_api.models import User


class RegisterFarmerViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterFarmerSerializer

    def get_queryset(self):
        return User.objects.filter(is_farmer=True)


#
# class CropViewSet(viewsets.ModelViewSet):
#     """
#     CRUD Operation for Crop endpoint
#     """
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = CropSerializer
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Crop, id=self.kwargs.get('pk'))
#
#     def get_queryset(self):
#         return Crop.objects.all()
#
#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.serializer_class(data=request.data)
#
#             if serializer.is_valid(raise_exception=True):
#                 farmer = get_object_or_404(Farmer, user=request.user)
#                 new_crop = Crop.objects.create(farmer=farmer, **serializer.data)
#                 new_crop.save()
#
#                 data = {
#                     "farmer_name": f"{new_crop.farmer.first_name} {new_crop.farmer.last_name}",
#                     "crop_name": new_crop.crop_name,
#                     "quantity": new_crop.quantity,
#                     "price": new_crop.price,
#                     "discount": new_crop.discount,
#                     "delivery_type": new_crop.delivery_type,
#                 }
#                 return response.Response(data, status=status.HTTP_201_CREATED)
#         except Exception:
#             return response.Response(data={"message": f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
#
#         return response.Response(data={"message": f"Not authorized"}, status=status.HTTP_400_BAD_REQUEST)
#

class FarmersViewSet(viewsets.ModelViewSet):
    """
    CRUD Operation for Farmers endpoint
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FarmerSerializer

    def get_object(self, queryset=None):
        return get_object_or_404(Farmer, id=self.kwargs.get('pk'))

    def get_queryset(self):
        return Farmer.objects.all()

