
from django.shortcuts import render, redirect

def login(request):
    return render(request, 'login.html')

        
def logout(request):
    return render(request, 'logout.html')
    

def pagina_inexistente(request, exception):  # precisa ser exception
    return render(request, 'pagina-inexistente.html')


def suporte(request):
    return render(request, 'suporte.html')

def base(request):
    return render(request, 'base.html')

def atualizar_dados(request):
    return render(request, 'atualizar_dados.html')

def recup_senha(request):
    return render(request, 'recup_senha.html')

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')


def altera_senha(request):
    return render(request, 'altera_senha.html')
