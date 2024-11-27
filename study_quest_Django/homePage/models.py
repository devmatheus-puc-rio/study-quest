from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    periodo = models.IntegerField()
    xp = models.IntegerField()

    def __str__(self):
        return self.nome

class PlanoDeEstudo(models.Model):
    identificacao = models.IntegerField()
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    avaliacao = models.FloatField()
    visibilidade = models.CharField(max_length=50)
    data = models.DateField(max_length=10)
    nVisualizacoes = models.IntegerField(default=0)
    nFavoritos = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class SecaoDeEstudo(models.Model):
    numeracao = models.IntegerField()
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    valorXp = models.IntegerField()

    def __str__(self):
        return self.titulo
    
class MaterialDeEstudo(models.Model):
    numeracao = models.IntegerField()
    titulo = models.CharField(max_length=200)
    valorXp = models.IntegerField()
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo
    
class Arquivo(models.Model):
    identificacao = models.IntegerField()
    link = models.FilePathField()

    def __str__(self):
        return self.link
    
class Quizzes(models.Model):
    def __str__(self):
        return self
    
class Pergunta(models.Model):
    identificacao = models.IntegerField()
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto
    
class Resposta(models.Model):
    identificacao = models.IntegerField()
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto

# Create your models here.
