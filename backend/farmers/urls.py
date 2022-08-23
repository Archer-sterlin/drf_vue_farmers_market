from rest_framework.routers import DefaultRouter

from .views import FarmersViewSet, RegisterFarmerViewSet

app_name = "farmers_api"

router = DefaultRouter()
router.register("farmer/register", RegisterFarmerViewSet, basename="register_farmer")
router.register("farmers", FarmersViewSet, basename="farmers_endpoint")

urlpatterns = router.urls
