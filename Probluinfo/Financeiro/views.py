from django.shortcuts import render, redirect
from django.db import transaction
from Financeiro.models import Caixa
from Financeiro.forms import FormCaixa
from django.views.decorators.http import require_POST
from ViewsProject.views import efetua_paginacao


# Create your views here.
def cadastra_lancamentos(request):
    tipo = Caixa.TIPOS_CHOICES
    if request.method == 'POST':
        caixa = FormCaixa(request.POST or None)
        if caixa.is_valid():
            caixa.save()
        return redirect(cadastra_lancamentos)
    dados = {
        'tipo':tipo,
    }
    return render(request,'cadastra_lancamentos.html',dados)

def lista_lancamentos(request):
    procura= request.GET.get('procura')
    if procura:
        caixa = Caixa.objects.filter(caixa__icontains=procura)
    else:
        caixa = Caixa.objects.all()
    
    total = caixa.count

    dados = {
                'caixas' : caixa,
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, caixa)
            }

    return render(request,'lista_lancamentos.html',dados)

def altera_lancamentos(request):
    return render(request,'altera_lancamentos.html')

