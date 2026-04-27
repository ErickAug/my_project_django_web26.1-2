from django.db import models

# Create your models here.
class Certificado(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

class Projeto(models.Model):
    tipo = models.CharField(max_length=30)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    git = models.URLField()

    def __str__(self):
        return self.nome