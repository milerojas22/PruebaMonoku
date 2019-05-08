from django.shortcuts import render
from .models import Participante
from .models import Producto
from .models import Productosconsumido
from .forms import Productosconsumidoform
from django.http import HttpResponse


def productosconsumidos(request):
    nombre='Julian'

    if request.method == "POST":
        form = Productosconsumidoform(request.POST)
        if form.is_valid():
            productosconsumidos = form.save()
            form = Productosconsumidoform()
    else:
        form = Productosconsumidoform()

    cantidad_producto = Productosconsumido.objects.all().count()
    ultimo_producto = Productosconsumido.objects.last()
    nombre_participante = ultimo_producto.nombre
    producto_consumido = ultimo_producto.nombreproducto

    return render(request, 'monoku/post_list.html', {'form': form, 'milena':nombre, 
        'cantidad_producto':cantidad_producto, 
        'nombre_participante':nombre_participante,
        'producto_consumido':producto_consumido})

# def listado_productos_consumidos(request):

    







