from django.shortcuts import render
from .models import ordem

def home(request):
    return render(request,'usuarios/home.html')

def ordens(request):
    nova_ordem = ordem()
    nova_ordem.nome = request.POST.get('nome')
    nova_ordem.descricao = request.POST.get('descricao')
    nova_ordem.responsavel = request.POST.get('responsavel')
    nova_ordem.save()

    ordens = {
        'ordens': ordem.objects.all()
    }

    return render(request,'usuarios/ordens.html', ordens)


