"""Probluinfo URL Configuration
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from core.views import suporte,base,base_gestao,base_pdv,login,sobre,recup_senha,atualizar_dados,altera_senha



from Cursos.views import cadastra_cursos,cadastra_salas,cadastra_notas,cadastra_matriculas
from Cursos.views import exclui_cursos,exclui_salas,exclui_notas,exclui_matriculas
from Cursos.views import lista_cursos,lista_salas,lista_notas,lista_matriculas
from Cursos.views import altera_cursos,altera_salas,altera_notas,altera_matriculas


from Financeiro.views import cadastra_lancamentos
from Financeiro.views import exclui_lancamentos
from Financeiro.views import lista_lancamentos
from Financeiro.views import altera_lancamentos


from Pessoas.views import cadastra_pessoas
from Pessoas.views import exclui_pessoas
from Pessoas.views import lista_pessoas
from Pessoas.views import altera_pessoas

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('altera-pessoas',altera_pessoas, name='altera-pessoas'),
    path('altera-cursos',altera_cursos, name='altera-cursos'),
    path('altera-salas',altera_salas, name='altera-salas'),
    path('altera-notas',altera_notas, name='altera-notas'),
    path('altera-matriculas',altera_matriculas, name='altera-matriculas'),
    path('altera-lancamentos',altera_lancamentos, name='altera-lancamentos'),

    path('cadastra-pessoas',cadastra_pessoas, name='cadastra-pessoas'),
    path('cadastra-cursos',cadastra_cursos, name='cadastra-cursos'),
    path('cadastra-salas',cadastra_salas, name='cadastra-salas'),
    path('cadastra-notas',cadastra_notas, name='cadastra-notas'),
    path('cadastra-matriculas',cadastra_matriculas, name='cadastra-matriculas'),
    path('cadastra-lancamentos',cadastra_lancamentos, name='cadastra-lancamentos'),

    path('lista-pessoas',lista_pessoas, name='lista-pessoas'),
    path('lista-cursos',lista_cursos, name='lista-cursos'),
    path('lista-salas',lista_salas, name='lista-salas'),
    path('lista-notas',lista_notas, name='lista-notas'),
    path('lista-matriculas',lista_matriculas, name='lista-matriculas'),
    path('lista-lancamentos',lista_lancamentos, name='lista-lancamentos'),

    path('exclui-pessoas',exclui_pessoas, name='exclui-pessoas'),
    path('exclui-cursos',exclui_cursos, name='exclui-cursos'),
    path('exclui-salas',exclui_salas, name='exclui-salas'),
    path('exclui-notas',exclui_notas, name='exclui-notas'),
    path('exclui-matriculas',exclui_matriculas, name='exclui-matriculas'),
    path('exclui-lancamentos',exclui_lancamentos, name='exclui-lancamentos'),

    path('suporte',suporte, name='suporte'),
    path('base-gestao/',base_gestao, name = "base-gestao"),
    path('base-pdv/',base_pdv, name = "base-pdv"),
    path('base/',base, name = "base"),
    path("login/",login, name="login"),
    path("sobre/",sobre, name="sobre"),
    path('recup-senha/',recup_senha, name ="recup-senha"),
    path('login/recup-senha/',recup_senha, name ="recup-senha"),
    path('atualizar-dados/',atualizar_dados, name = "atualizar-dados"),
    path('altera-senha/',altera_senha, name = "altera-senha"),
    path('accounts/',include('django.contrib.auth.urls')),
    path("",login, name="login"),
]
handler404 = 'core.views.pagina_inexistente'
    
