from django.urls import path
from . import views

urlpatterns = [
    path('', views.participante_lista, name='participante_lista'),
    path('productoscon/new', views.productosconsumidos, name='productoscon_new'),
]