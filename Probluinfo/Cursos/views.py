from django.shortcuts import render

# Create your views here.
def cadastra_salas(request):
    return render(request,'cadastra_salas.html')

def cadastra_cursos(request):
    return render(request,'cadastra_cursos.html')

def cadastra_matriculas(request):
    return render(request,'cadastra_matriculas.html')

def cadastra_notas(request):
    return render(request,'cadastra_notas.html')