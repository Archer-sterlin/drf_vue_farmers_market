from .views import OrderViewSet, OrderItemViewSet
from rest_framework.routers import DefaultRouter

app_name = 'order_api'

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')
router.register('farmer/crops', OrderItemViewSet, basename='order_item')

urlpatterns = router.urls
