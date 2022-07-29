from django.forms import ModelForm
from Pessoas.models import Pessoas

class FormPessoas(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['id','nm_completo','cpf','email','dt_nascimento','celular','fone_res','nm_resp','login','senha','perfil']
        db_table = 'Pessoas'
        
