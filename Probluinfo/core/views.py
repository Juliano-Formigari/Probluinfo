
from django.shortcuts import render, redirect

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')
    
def pagina_inexistente(request, exception):  # precisa ser exception
    return render(request, 'pagina-inexistente.html')

def suporte(request):
    return render(request, 'suporte.html')

def base_gestao(request):
    return render(request, 'base_gestao.html')

def base_pdv(request):
    return render(request, 'base_pdv.html')

def atualizar_dados(request):
    return render(request, 'atualizar_dados.html')

def recup_senha(request):
    return render(request, 'recup_senha.html')

def altera_senha(request):
    return render(request, 'altera_senha.html')

def sobre(request):
    return render(request, 'sobre.html')


def cadastra_alunos(request):
    return render(request, 'cadastra_alunos.html')

