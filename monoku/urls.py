from django.urls import path
from . import views

urlpatterns = [
    path('', views.participante_lista, name='participante_lista')
]