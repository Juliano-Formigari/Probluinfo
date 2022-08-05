"""Probluinfo URL Configuration
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from core import views


# from Cursos.views import cadastra_cursos

# from Financeiro.views import cadastra_lancamentos

# from Matriculas.views import cadastra_matriculas

# from Notas.views import cadastra_notas

# from Pessoas.views import cadastra_pessoas

# from Salas.views import cadastra_salas




urlpatterns = [

    path('admin/', admin.site.urls),
    path('suporte',views.suporte, name='suporte'),
    path('cadastra-alunos',views.cadastra_alunos),
    path('logout/',views.logout, name = "logout"),
    path('base_gestao/',views.base_gestao, name = "base_gestao"),
    path('base_pdv/',views.base_pdv, name = "base_pdv"),
    path("login/", views.login, name="login"),
    path("sobre/", views.sobre, name="sobre"),
    path('recup_senha/',views.recup_senha, name = "recup_senha"),
    path('atualizar_dados/',views.atualizar_dados, name = "atualizar_dados"),
    path('altera_senha/',views.altera_senha, name = "altera_senha"),
    path("", views.login, name="login"),
    
 
]

    
