"""Probluinfo URL Configuration
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from core import views


from Cursos.views import cadastra_cursos,altera_cursos,lista_cursos,exclui_cursos,cadastra_salas,altera_salas,lista_salas,exclui_salas,cadastra_notas,altera_notas,lista_notas,exclui_notas,cadastra_matriculas,altera_matriculas,lista_matriculas,exclui_matriculas

from Financeiro.views import cadastra_lancamentos,lista_lancamentos,altera_lancamentos,exclui_lancamentos

from Pessoas.views import lista_pessoas,cadastra_pessoas,altera_pessoas,exclui_pessoas


urlpatterns = [

    path('admin/', admin.site.urls),
    

    path('altera_pessoas',altera_pessoas, name='altera_pessoas'),
    path('altera_cursos',altera_cursos, name='altera_cursos'),
    path('altera_salas',altera_salas, name='altera_salas'),
    path('altera_notas',altera_notas, name='altera_notas'),
    path('altera_matriculas',altera_matriculas, name='altera_matriculas'),
    path('altera_lancamentos',altera_lancamentos, name='altera_lancamentos'),

    path('cadastra_pessoas',cadastra_pessoas, name='cadastra_pessoas'),
    path('cadastra_cursos',cadastra_cursos, name='cadastra_cursos'),
    path('cadastra_salas',cadastra_salas, name='cadastra_salas'),
    path('cadastra_notas',cadastra_notas, name='cadastra_notas'),
    path('cadastra_matriculas',cadastra_matriculas, name='cadastra_matriculas'),
    path('cadastra_lancamentos',cadastra_lancamentos, name='cadastra_lancamentos'),

    path('lista_pessoas',lista_pessoas, name='lista_pessoas'),
    path('lista_cursos',lista_cursos, name='lista_cursos'),
    path('lista_salas',lista_salas, name='lista_salas'),
    path('lista_notas',lista_notas, name='lista_notas'),
    path('lista_matriculas',lista_matriculas, name='lista_matriculas'),
    path('lista_lancamentos',lista_lancamentos, name='lista_lancamentos'),

    path('exclui_pessoas',exclui_pessoas, name='exclui_pessoas'),
    path('exclui_cursos',exclui_cursos, name='exclui_cursos'),
    path('exclui_salas',exclui_salas, name='exclui_salas'),
    path('exclui_notas',exclui_notas, name='exclui_notas'),
    path('exclui_matriculas',exclui_matriculas, name='exclui_matriculas'),
    path('exclui_lancamentos',exclui_lancamentos, name='exclui_lancamentos'),

    path('suporte',views.suporte, name='suporte'),
    path('logout/',views.logout, name = "logout"),
    path('base_gestao/',views.base_gestao, name = "base_gestao"),
    path('base_pdv/',views.base_pdv, name = "base_pdv"),
    path("login/", views.login, name="login"),
    path("sobre/", views.sobre, name="sobre"),
    path('recup_senha/',views.recup_senha, name = "recup_senha"),
    path('atualizar_dados/',views.atualizar_dados, name = "atualizar_dados"),
    path('altera_senha/',views.altera_senha, name = "altera_senha"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", views.login, name="login"),
    
 
]

    
