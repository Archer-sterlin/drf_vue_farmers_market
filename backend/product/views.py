from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import response, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from farmers.models import Farmer

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CropViewSet(viewsets.ModelViewSet):
    """
    CRUD Operation for Crop endpoint
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer

    def get_object(self, queryset=None):
        return get_object_or_404(Product, id=self.kwargs.get("pk"))

    def get_queryset(self):
        return Product.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid(raise_exception=True):
                farmer = get_object_or_404(Farmer, user=request.user)
                new_crop = Product.objects.create(farmer=farmer, **serializer.data)
                new_crop.save()

                data = {
                    "farmer_name": f"{new_crop.farmer.first_name} {new_crop.farmer.last_name}",
                    "crop_name": new_crop.crop_name,
                    "quantity": new_crop.quantity,
                    "price": new_crop.price,
                    "discount": new_crop.discount,
                    "delivery_type": new_crop.delivery_type,
                }
                return response.Response(data, status=status.HTTP_201_CREATED)
        except Exception:
            return response.Response(
                data={"message": f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
            )

        return response.Response(
            data={"message": f"Not authorized"}, status=status.HTTP_400_BAD_REQUEST
        )


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(["POST"])
def search(request):
    query = request.data.get("query", "")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
