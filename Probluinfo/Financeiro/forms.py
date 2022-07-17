from django.forms import ModelForm
from random import choices
from django.db import models
from .models import Caixa

class FormCaixa(ModelForm):
    model = Caixa
    fields = ['id','tipo','id_pessoa','descricao','valor','dt_lancamento']
    db_table = 'Caixa'