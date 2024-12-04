from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("planos/", views.planos, name="Planos"),
    path("criarPlanos", views.criarPlanos, name="Criar Planos")
]