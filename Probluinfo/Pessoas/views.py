from django.shortcuts import render, redirect
from Pessoas.models import Pessoas
from Pessoas.forms import FormPessoas

# Create your views here.
def cadastra_pessoas(request):
    perfis = Pessoas.PERFIS_CHOICES

    if request.method == 'POST':
        # perfil = request.POST.get('perfil')
        form = FormPessoas(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_pessoas)

    dados = {
                'perfis' : perfis,
                # 'perfil' : request.POST.get('perfil'),
            }

    return render(request,'cadastra_pessoas.html', dados)

def lista_pessoas(request):
    tipoPessoa = Pessoas.objects.all()

    dados = {
                'tipos' : tipoPessoa,
            }

    return render(request, 'lista_pessoas.html', dados)