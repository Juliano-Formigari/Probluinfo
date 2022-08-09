from django.shortcuts import render

# Create your views here.
def cadastra_pessoas(request):
    return render(request,'cadastra_pessoas.html')

def lista_pessoas(request):
    return render(request,'lista_pessoas.html')

def altera_pessoas(request):
    return render(request,'altera_pessoas.html')

def exclui_pessoas(request):
    return render(request,'exclui_pessoas.html')