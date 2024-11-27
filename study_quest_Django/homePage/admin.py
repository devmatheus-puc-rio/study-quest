from django.contrib import admin
from .models import Usuario, PlanoDeEstudo, Categoria, SecaoDeEstudo, MaterialDeEstudo, Arquivo, Quizzes, Pergunta, Resposta

# Register your models here.

admin.site.register(Usuario)
admin.site.register(PlanoDeEstudo)
admin.site.register(Categoria)
admin.site.register(SecaoDeEstudo)
admin.site.register(MaterialDeEstudo)
admin.site.register(Arquivo)
admin.site.register(Quizzes)
admin.site.register(Pergunta)
admin.site.register(Resposta)