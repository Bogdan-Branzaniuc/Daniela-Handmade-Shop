from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('admin_crud_products', views.admin_crud_products, name='admin_crud_products'),
    path('add_product_sizes_colors_categories', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
