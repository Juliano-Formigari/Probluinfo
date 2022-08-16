from http.client import HTTPResponse
from django.shortcuts import render, redirect
from Pessoas.models import Pessoas
from Pessoas.forms import FormPessoas
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from ViewsProject.views import efetua_paginacao

# Create your views here.
def cadastra_pessoas(request):
    perfis = Pessoas.PERFIS_CHOICES
    if request.method == 'POST':
        form = FormPessoas(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(cadastra_pessoas)

        if request.method == "GET":
            return render(request,'cadastro.pessoas.html')
        else:
            login = request.POST.get('login')
            senha = request.POST.get('senha')
            email = request.POST.get('email')
            login = User.objects.get(login=login)
            login = User.objects.create_user(login=login, email=email, password=senha)
            login.save()

            return HTTPResponse(login)  

    dados = {
        'perfis' : perfis,
            }
    
    return render(request,'cadastra_pessoas.html', dados)

def lista_pessoas(request):
    procura = request.GET.get('procura')
    tipoPessoa = Pessoas.objects.all()

    total = tipoPessoa.count

    dados = {
                'tipos' : tipoPessoa,
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, tipoPessoa)
                
            }

    return render(request, 'lista_pessoas.html', dados)
    
def altera_pessoas(request,id):
    pessoas = Pessoas.objects.get(id=id)
    data_nas = pessoas.dt_nascimento
    data_nas = data_nas.strftime('%Y-%m-%d')
    if request.method == 'POST':
        form = FormPessoas(request.POST, instance=pessoas)
        if form.is_valid():
            form.save()
            return redirect(lista_pessoas)
    return render(request, 'altera_pessoas.html', {'pessoas' : pessoas,'data_nas':data_nas})
   

def exclui_pessoas(request,id):
    pessoas = Pessoas.objects.get(id=id)
    if request.method == 'POST':
        pessoas.delete()
        return redirect(lista_pessoas)

    return render(request,'exclui_pessoas.html' , {'tipo' : pessoas})