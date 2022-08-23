from django.shortcuts import get_object_or_404
from rest_framework import authentication, response, status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from product.models import Product

from .models import Order
from .serializers import OrderItemSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = OrderSerializer

    def get_object(self, queryset=None):
        return get_object_or_404(Order, id=self.kwargs.get("pk"))

    def get_queryset(self):
        return Order.objects.all(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid(raise_exception=True):
                new_order = Product.objects.create(user=request.user, **serializer.data)
                new_order.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return response.Response(
                data={"message": f"Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
            )

        return response.Response(
            data={"message": f"Not authorized"}, status=status.HTTP_400_BAD_REQUEST
        )


class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = OrderSerializer
