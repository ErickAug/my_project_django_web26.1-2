from django.db import models
from django.conf import settings

# Create your models here.
class Pessoal(models.Model):

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil',
        null=True,
        blank=True,
    )

    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=3)
    email = models.EmailField()
    git = models.URLField()
    linkedin = models.URLField()
    image = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Perfil Pessoal'
        verbose_name_plural = 'Perfis Pessoais'

    def __str__(self):
        return self.nome