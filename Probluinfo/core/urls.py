"""Probluinfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cursos.views import cadastra_salas,cadastra_cursos,cadastra_matricula,cadastra_notas
from Pessoas.views import cadastra_pessoa
from Financeiro.views import cadastra_lancamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastra-salas',cadastra_salas),
    path('cadastra-cursos',cadastra_cursos),
    path('cadastra-matricula',cadastra_matricula),
    path('cadastra-notas',cadastra_notas),
    path('cadastra-pessoa',cadastra_pessoa),
    path('cadastra-lancamento',cadastra_lancamento),
]
