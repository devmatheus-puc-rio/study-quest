from django.shortcuts import render, HttpResponse
from .models import PlanoDeEstudo

# Create your views here.
def home(request):
    return render(request, "home.html")

def planos(request):
    items = PlanoDeEstudo.objects.all()
    return render(request, "planosdeestudo.html", {"planos": items})