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

def lista_cursos(request):
    return render(request,'lista_cursos.html')

def lista_matriculas(request):
    return render(request,'lista_matriculas.html')

def lista_notas(request):
    return render(request,'lista_notas.html')

def lista_salas(request):
    return render(request,'lista_salas.html')

def altera_matriculas(request):
    return render(request,'altera_matriculas.html')

def altera_salas(request):
    return render(request,'altera_salas.html')

def altera_cursos(request):
    return render(request,'altera_cursos.html')

def altera_notas(request):
    return render(request,'altera_notas.html')

def exclui_notas(request):
    return render(request,'exclui_notas.html')

def exclui_cursos(request):
    return render(request,'exclui_cursos.html')

def exclui_salas(request):
    return render(request,'exclui_salas.html')

def exclui_matriculas(request):
    return render(request,'exclui_matriculas.html')







