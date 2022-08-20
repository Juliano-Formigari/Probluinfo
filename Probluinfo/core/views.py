from django.shortcuts import render, redirect

def pagina_inexistente(request, *args, **argv):# precisa ser exception
    return render(request, 'pagina_inexistente.html',status=404)

def nao_autorizado(request, *args, **argv):  # precisa ser exception
    return render(request, 'nao_autorizado.html',status=401)

def erro_servidor(request, *args, **argv):
    return render(request, 'erro_servidor.html', status=500)