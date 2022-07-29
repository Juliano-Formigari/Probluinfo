from django.forms import ModelForm
from Financeiro.models import Caixa

class FormCaixa(ModelForm):
    class Meta:
        model = Caixa
        fields = ['id','tipo','descricao','valor','dt_lancamento','id_pessoa']
        db_table = 'Caixa'