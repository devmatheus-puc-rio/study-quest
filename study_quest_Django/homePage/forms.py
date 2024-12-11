from django.forms import ModelForm
from django import forms
from .models import PlanoDeEstudo

escolhasVisibilidades = {
    (2, "Visivel"),
    (1, "Restrito"),
    (0, "Privado")
}

class CriarPlanoForm(forms.Form):
    titulo = forms.CharField()
    descricao = forms.CharField()
    visibilidade = forms.ChoiceField(choices=escolhasVisibilidades)
    class Meta:
        model = PlanoDeEstudo
        fields = ['titulo','descricao','visibilidade']