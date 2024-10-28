from django.db import models

class PlanoDeEstudo(models.Model):
    titulo = models.CharField(max_length=200)
    completo = models.BooleanField(default=False)

# Create your models here.
