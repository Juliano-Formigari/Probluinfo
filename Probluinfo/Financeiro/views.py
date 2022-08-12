from django.shortcuts import render
from Financeiro.models import Caixa
from Financeiro.forms import FormCaixa
# Create your views here.
def cadastra_lancamentos(request):
    tipo = Caixa.TIPOS_CHOICES
    if request.method == 'POST':
        form = FormCaixa(request.POST or None)
        if form.is_valid():
            form.save()
    dados = {
        'tipo':tipo,
    }
    return render(request,'cadastra_lancamentos.html',dados)

def lista_lancamentos(request):
    return render(request,'lista_lancamentos.html')

def altera_lancamentos(request):
    return render(request,'altera_lancamentos.html')

def exclui_lancamentos(request):
    return render(request,'exclui_lancamentos.html')