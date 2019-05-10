from django import forms
from .models import Productosconsumido
from .models import Producto



class Productosconsumidoform(forms.ModelForm):
    
    class Meta:
        model = Productosconsumido
        fields = ('nombre', 'nombreproducto','cantidadconsumida')


class InventarioFinalform(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombreproducto','cantidad','fechavencimiento')


