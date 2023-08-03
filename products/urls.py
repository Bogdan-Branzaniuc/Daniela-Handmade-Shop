from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('admin_crud_products', views.admin_crud_products, name='admin_crud_products')
]
