from rest_framework.routers import DefaultRouter

from .views import CropViewSet, RegisterFarmerViewSet

app_name = "farmers_api"

router = DefaultRouter()
router.register("farmer/register", RegisterFarmerViewSet, basename="farmers_endpoint")
router.register("farmer/crops", CropViewSet, basename="crop_endpoint")

urlpatterns = router.urls

