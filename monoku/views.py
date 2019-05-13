from django.shortcuts import render
from .models import Participante
from .models import Producto
from .models import Productosconsumido
from .forms import Productosconsumidoform
from .forms import InventarioFinalform
from django.http import HttpResponse
from django.db.models import Sum
from django.contrib import messages


def productosconsumidos(request):

    if request.method == "POST":
        form = Productosconsumidoform(request.POST)

        if form.is_valid():
            if form.cleaned_data['nombreproducto'].cantidad >= form.cleaned_data['cantidadconsumida']:
                productosconsumidos = form.save()
                productosconsumidos.nombreproducto.cantidad -= productosconsumidos.cantidadconsumida
                productosconsumidos.nombreproducto.save()
                form = Productosconsumidoform()

            else:
                messages.add_message(request, messages.INFO, 'Producto agotado')
    else:
        
        form = Productosconsumidoform()

    cantidad_producto = Productosconsumido.objects.aggregate(total_sum=Sum('cantidadconsumida'))
    ultimo_producto = Productosconsumido.objects.last()
    nombre_participante = ultimo_producto.nombre
    producto_consumido = ultimo_producto.nombreproducto



    return render(request, 'monoku/post_list.html', {'form':form,
        'cantidad_producto':cantidad_producto['total_sum'],
        'nombre_participante':nombre_participante,
        'producto_consumido':producto_consumido})



def listado_productos_consumidos(request):

    if request.method == "POST":
        form2 = InventarioFinalform(request.POST)
        if form.is_valid():
            producto = form2.save()
            form2 = InventarioFinalform()
    else:
        form = InventarioFinalform()

    nombreproducto = list(Producto.objects.all())
    cantidad = list(Producto.objects.all())
    fechavencimiento = list(Producto.objects.all())


    return render(request, 'monoku/Inventory.html', {'form2': form, 
        'nombreproducto':nombreproducto, 
        'cantidad':cantidad,
        'fechavencimiento':fechavencimiento})



    





