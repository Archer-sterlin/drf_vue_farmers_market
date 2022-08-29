from django.urls import path

from product import views

app_name = "products"

urlpatterns = [
    path('products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<str:category_name>/', views.CategoryDetail.as_view()),
]