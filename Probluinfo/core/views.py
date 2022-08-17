
from http.client import HTTPResponse
import time
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django
from django.contrib.auth import logout 


def login(request):
    if request.user.is_authenticated:
        return redirect('base-pbi')
    else:
        if request.method=='POST':
            login=request.POST.get('login')
            senha = request.POST.get('senha')
        
            user = authenticate(request, username=login, password=senha)
            
            if user is not None :
                login_django(request,user)
                
                if request.POST.get('setor')=="pdv":
                    request.session['base']="pdv"

                else:
                    request.session['base']="gestao"
                return redirect('base-pbi')

        return render (request,'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')
        

def pagina_inexistente(request, exception):  # precisa ser exception
    return render(request, 'pagina_inexistente.html')

def suporte(request):
    return render(request, 'suporte.html')

def base_pbi(request):
    print(request.user.first_name)
    return render(request, 'base_pbi.html')

def atualizar_dados(request):
    return render(request, 'atualizar_dados.html')

def recup_senha(request):
    return render(request, 'recup_senha.html')

def altera_senha(request):
    return render(request, 'altera_senha.html')

def sobre(request):
    return render(request, 'sobre.html')

