from django.shortcuts import render
from .models import Participante
from .models import Producto
from .forms import Productosconsumidoform
# Create your views here.
def participante_lista(request):
    participantes = Participante.objects.all()
    productos = Producto.objects.all()
    return render(request, 'monoku/post_list.html', {'participantes':participantes, 'productos':productos})

def productosconsumidos(request):
    if request.method == "POST":
        form = Productosconsumidoform(request.POST)
        if form.is_valid():
            productosconsumidos = form.save(commit=False)
            productosconsumidos.save()

    else:
        form = Productosconsumidoform()
    return render(request, 'monoku/post_list.html', {'form': form})