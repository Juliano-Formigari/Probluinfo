from django.shortcuts import render

# Create your views here.
def cadastra_lancamentos(request):
    return render(request,'cadastra_lancamentos.html')

def lista_lancamentos(request):
    return render(request,'lista_lancamentos.html')

def altera_lancamentos(request):
    return render(request,'altera_lancamentos.html')

def exclui_lancamentos(request):
    return render(request,'exclui_lancamentos.html')