from django.urls import path

from order import views

app_name = "orders"

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),  
]