from django.contrib import admin
from .models import Participante
from .models import Producto
from .models import Productosconsumido



admin.site.register(Participante)
admin.site.register(Producto)
admin.site.register(Productosconsumido)