from django.shortcuts import render

# Create your views here.

def telaCadastro(request):
    return render(request, "tela-cadastro.html")
