from django.shortcuts import render,redirect
from Cursos.forms import FormCursos,FormMatriculas,FormNotas,FormSalas
from Cursos.models import Matriculas,Cursos,Salas,Notas

# Create your views here.

def cadastra_cursos(request):
    if request.method == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'cadastra_cursos.html')
    
def cadastra_matriculas(request):
    periodos = Matriculas.PERIODOS_CHOICES
    if request.method == 'POST':
        form = FormMatriculas(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(cadastra_matriculas)

    dados = {
                'periodos': periodos,
            }
    return render(request,'cadastra_matriculas.html', dados)

def cadastra_salas(request):
    if request.method == 'POST':
        form = FormSalas(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'cadastra_salas.html')

def cadastra_notas(request):
    if request.method == 'POST':
        form = FormNotas(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'cadastra_notas.html')


def lista_cursos(request):
    tipoCurso = Cursos.objects.all()

    dados = {
                'tipos' : tipoCurso,
            }

    return render(request,'lista_cursos.html')

def lista_matriculas(request):
    procura = request.GET.get('procura')

    if procura:
        matricula = Matriculas.objects.filter(nome__icontains=procura)|Matriculas.objects.filter(email__icontains=procura)
    else:
        matricula = Matriculas.objects.all()

    total = matricula.count

    dados = {
                'matricula' : matricula, 
                'total' : total, 
                'procura' : procura,
              
            }

    return render(request, 'lista_matriculas.html', dados)

def lista_notas(request):
    return render(request,'lista_notas.html')

def lista_salas(request):
    return render(request,'lista_salas.html')


def altera_cursos(request):
    return render(request,'altera_cursos.html')

def altera_matriculas(request):
    return render(request,'altera_matriculas.html')

def altera_notas(request):
    return render(request,'altera_notas.html')

def altera_salas(request):
    return render(request,'altera_salas.html')



def exclui_cursos(request):
    return render(request,'exclui_cursos.html')

def exclui_matriculas(request):
    return render(request,'exclui_matriculas.html')
def exclui_notas(request):
    return render(request,'exclui_notas.html')

def exclui_salas(request):
    return render(request,'exclui_salas.html')







