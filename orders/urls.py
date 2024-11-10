from django.urls import path
from . import views

urlpatterns = [
    path('create-from-product/<int:product_id>/', views.create_order_from_product, name='create_order_from_product'),
    path('order-success/', views.order_success, name='order_success'),


]
