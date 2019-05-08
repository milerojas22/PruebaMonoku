from django import forms

from .models import Productosconsumido

class Productosconsumidoform(forms.ModelForm):
    
    class Meta:
        model = Productosconsumido
        fields = ('nombre', 'nombreproducto','cantidadconsumida')

