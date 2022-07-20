"""Probluinfo URL Configuration
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from Cursos.views import cadastra_salas,cadastra_cursos,cadastra_matriculas,cadastra_notas
from Pessoas.views import cadastra_pessoas
from Financeiro.views import cadastra_lancamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastra-salas',cadastra_salas),
    path('cadastra-cursos',cadastra_cursos),
    path('cadastra-matriculas',cadastra_matriculas),
    path('cadastra-notas',cadastra_notas),
    path('cadastra-pessoas',cadastra_pessoas),
    path('cadastra-lancamento',cadastra_lancamento),
]
