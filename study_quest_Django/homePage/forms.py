from django.forms import ModelForm
from django import forms
from models import PlanoDeEstudo

class CriarPlanoForm(ModelForm):
    titulo = forms.TextInput()
    descricao = forms.TextInput()
    visibilidade = forms.TextInput()
    class Meta:
        model = PlanoDeEstudo
        fields = ['titulo','descricao','visibilidade']