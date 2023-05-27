from django.urls import path
from . import views

urlpatterns = [
    path('', views.food),
    path("cart/",views.add_cart),
    path('view/<int:pk>/', views.food_detail),
    path('add_cart/<int:pk>/', views.add_to_cart),
    path('delete_cart/<int:pk>/', views.delete_cart_item),
]
