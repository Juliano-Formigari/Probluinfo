
from http.client import HTTPResponse
import time
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django
from django.contrib.auth import logout 


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        login=request.POST.get('login')
        senha = request.POST.get('senha')

        login = authenticate(login=login, password=senha)

        if login:
            login_django(request,login)

            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')
        

def pagina_inexistente(request, exception):  # precisa ser exception
    return render(request, 'pagina-inexistente.html')

def suporte(request):
    return render(request, 'suporte.html')

def base_gestao(request):
    return render(request, 'base_gestao.html')

def base(request):
    return render(request, 'base.html')

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

