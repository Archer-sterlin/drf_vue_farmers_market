from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

schema_view = get_schema_view(
    openapi.Info(
        title="Farmers Market API",
        default_version="v1",
        description="Provides CRUDE operation to help farms manager their crops",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="wistler4u@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # SWAGGER DOCUMENTATION
    path("swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("doc/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Oauth2
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # custom urls
    path("api/v1/", include("auth_api.urls",namespace="user_api")),
    path("api/v1/", include("farmers.urls", namespace="farmers_api")),
    path("api/v1/", include("product.urls", namespace="product_api")),
    path("api/v1/", include("order.urls", namespace="order_api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
