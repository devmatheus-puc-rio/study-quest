from django.shortcuts import render, HttpResponse
from .models import PlanoDeEstudo

# Create your views here.
def home(request):
    items = PlanoDeEstudo.objects.all()
    return render(request, "home.html", {"planos": items})

def planos(request):
    items = PlanoDeEstudo.objects.all()
    return render(request, "planosdeestudo.html", {"planos": items})