from django.forms import ModelForm
from .models import Pessoas,Perfis


class FormPessoas(ModelForm):
    model = Pessoas
    fields = ['id','nm_completo','cpf','email','dt_nascimento','celular','fone_res','nm_resp','dt_alteracao','login','senha','contato','perfil','dt_alteracao']
    db_table = 'Pessoas'

# Nova tabela abaixo
        

class ForPerfis(ModelForm):
    model = Perfis
    fields = ['id','ds_perfil']
    db_table = 'Perfis'