from django.urls import path

from .views import RegisterView

app_name = "auth_api"

urlpatterns = [path("user/register/", RegisterView.as_view(), name="register")]
