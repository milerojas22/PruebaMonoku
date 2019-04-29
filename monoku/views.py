from django.shortcuts import render
from .models import Participante
from .models import Producto
# Create your views here.
def participante_lista(request):
    participantes = Participante.objects.all()
    productos = Producto.objects.all()
    return render(request, 'monoku/post_list.html', {'participantes':participantes, 'productos':productos})

