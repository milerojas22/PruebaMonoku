from django.urls import path
from . import views

urlpatterns = [

    path('', views.productosconsumidos, name='productoscon_new'),
]