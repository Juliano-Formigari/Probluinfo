"""Probluinfo URL Configuration
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Cursos.views import cadastra_salas,cadastra_cursos,cadastra_matriculas,cadastra_notas
from Pessoas.views import cadastra_pessoas
from Financeiro.views import cadastra_lancamento
from django.views.generic import TemplateView
from core import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('suporte',views.suporte, name='suporte'),
    path('cadastra-salas',cadastra_salas),
    path('cadastra-cursos',cadastra_cursos),
    path('cadastra-matriculas',cadastra_matriculas),
    path('cadastra-notas',cadastra_notas),
    path('cadastra-pessoas',cadastra_pessoas),
    path('cadastra-lancamento',cadastra_lancamento),
    path('logout/',views.logout, name = "logout"),
    path('base/',views.base, name = "base"),
    path("login/", views.login, name="login"),
    path('index2/',views.index2, name = "index2"),
    path('index/',views.index, name = "index"),
    path('recup_senha/',views.recup_senha, name = "recup_senha"),
    path('atualizar_dados/',views.atualizar_dados, name = "atualizar_dados"),
    path('altera_senha/',views.altera_senha, name = "altera_senha"),
    
 
]

    
