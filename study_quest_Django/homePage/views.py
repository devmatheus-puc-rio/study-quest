from django.shortcuts import render, HttpResponse
from .models import PlanoDeEstudo
from .models import Categoria
import random

# Create your views here.
def home(request):
    items = list(PlanoDeEstudo.objects.all())
    items1 = random.sample(items, 3)
    items2 = random.sample(items, 3)
    items3 = random.sample(items, 3)
    categorias = list(Categoria.objects.all())
    categorias = random.sample(categorias, 5)
    return render(request, "home.html", {"planos1": items1,"planos2": items2,"planos3": items3, "categorias": categorias})

def planos(request):
    items = PlanoDeEstudo.objects.all()
    return render(request, "planosdeestudo.html", {"planos": items})

def criarPlanos(request):
    categorias = list(Categoria.objects.all())
    categorias = random.sample(categorias, 5)
    return render(request, "criarPlano.html", {"categorias": categorias})