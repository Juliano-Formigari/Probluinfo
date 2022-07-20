from django.shortcuts import render

# Create your views here.
def cadastra_pessoas(request):
    return render(request,'cadastra_pessoas.html')