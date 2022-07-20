from django.shortcuts import render

# Create your views here.
def cadastra_pessoa(request):
    return render(request,'cadastra_pessoa.html')

def login(request):
    return render(request,'login.html')