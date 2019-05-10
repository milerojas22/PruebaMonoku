from django.urls import path
from . import views

urlpatterns = [

    path('', views.productosconsumidos, name='productoscon_new'),
    path('inventario/', views.listado_productos_consumidos, name='inventory_new')
]