
from distutils.command.config import config
from http.client import HTTPResponse
import time
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from Pessoas.models import Pessoas
from django.contrib.auth import login as login_django
from django.contrib.auth import logout 
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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
    if request.method == "POST":
        POST = request.POST
        try:
            send_mail('Contato via Sistema', f"Mensagem Enviada de {POST['nome']}\n{POST['mensagem']}" , 'pbisistema@hotmail.com' , ['leandroslv125@gmail.com'],fail_silently=False) 
            messages.success(request,'Contato enviado com Sucesso')
        except BadHeaderError:
            messages.warning(request,'Contato não Enviado!')
    return render(request, 'suporte.html')

def base_pbi(request):
    return render(request, 'base_pbi.html')

def atualizar_dados(request):
    return render(request, 'atualizar_dados.html')

def recup_senha(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Pessoas.objects.filter(email=data)
            if associated_users.exists():
                token= default_token_generator.make_token(associated_users[0])
                uid = urlsafe_base64_encode(force_bytes(associated_users[0].pk))
                url= f"http://http://127.0.0.1:8000/reset/{uid}/{token}/"
                try:
                        send_mail('Resetar Senha', url, 'pbisistema@hotmail.com' , [associated_users[0].email], fail_silently=False)
                        messages.success(request,'Email enviado com Sucesso')
                except BadHeaderError:
                        messages.warning(request,'Email não Localizado!')

    return render(request, 'recup_senha.html')

def altera_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('base-pbi')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'altera_senha.html', {'form': form})


def sobre(request):
    return render(request, 'sobre.html')

