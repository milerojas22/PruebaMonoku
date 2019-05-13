from django.urls import path
from . import views

urlpatterns = [

    path('comer/', views.productosconsumidos, name='productoscon_new'),
    path('', views.listado_productos_consumidos, name='inventory_new')
]