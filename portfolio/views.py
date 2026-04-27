from django.shortcuts import render
from core.models import Pessoal
from .models import Projeto, Certificado

def home(request):
    pessoa = Pessoal.objects.first()
    certificados = Certificado.objects.all()
    return render(request, 'portfolio/home.html', {'pessoa':pessoa, 'certificado':certificados})


def projetos(request):
    projetos =  Projeto.objects.all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def contatos(request):
    pessoa = Pessoal.objects.first()
    return render(request, 'portfolio/contatos.html', {'pessoa': pessoa})