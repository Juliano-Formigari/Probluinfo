from django.shortcuts import render
from Cursos.forms import FormCursos

# Create your views here.
def cadastra_salas(request):
    return render(request,'cadastra_salas.html')

def cadastra_cursos(request):
    if request.method == 'POST':
        form = FormCursos(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'cadastra_cursos.html')

def cadastra_matriculas(request):
    return render(request,'cadastra_matriculas.html')

def cadastra_notas(request):
    return render(request,'cadastra_notas.html')