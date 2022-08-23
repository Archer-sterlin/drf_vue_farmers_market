from rest_framework.routers import DefaultRouter

from .views import CropViewSet

app_name = "product_api"

router = DefaultRouter()

router.register("farmer/products", CropViewSet, basename="crops_endpoint")

urlpatterns = router.urls
