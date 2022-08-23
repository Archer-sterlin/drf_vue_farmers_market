from .views import FarmersViewSet, RegisterFarmerViewSet
from rest_framework.routers import DefaultRouter

app_name = 'farmers_api'

router = DefaultRouter()
router.register('farmer/register', RegisterFarmerViewSet, basename='register_farmer')
router.register('farmers', FarmersViewSet, basename='farmers_endpoint')

urlpatterns = router.urls
