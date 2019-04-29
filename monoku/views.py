from django.shortcuts import render
from .models import *

# Create your views here.
def post_list(request):
    return render(request, 'monoku/post_list.html', {})
