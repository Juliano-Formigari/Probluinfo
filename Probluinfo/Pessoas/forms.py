from django.forms import ModelForm
from Pessoas.models import Pessoas


class FormPessoas(ModelForm):
    model = Pessoas
    fields = ['id','nm_completo','cpf','email','dt_nascimento','celular','fone_res','nm_resp','dt_alteracao','login','senha','contato','perfil','dt_alteracao']
    db_table = 'Pessoas'
        
