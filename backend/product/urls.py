from .views import CropViewSet
from rest_framework.routers import DefaultRouter


app_name = 'product_api'

router = DefaultRouter()

router.register('farmer/products', CropViewSet, basename='crops_endpoint')

urlpatterns = router.urls
