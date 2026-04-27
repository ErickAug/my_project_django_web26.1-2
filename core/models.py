from django.db import models

# Create your models here.
class Pessoal(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=3)
    email = models.EmailField()
    git = models.URLField()
    linkedin = models.URLField()
    image = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.nome