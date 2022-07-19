from random import choices
from django.db import models
from django.forms import CharField
from Pessoas.models import Pessoas

# Create your models here.
class Caixa(models.Model):
    Tipos = (
    ('1','Entrada'),
    ('2','Saída'),
    )
    tipo = models.CharField(max_length=1,choices=Tipos, blank=False)
    id_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, blank=False)
    valor = models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    dt_lancamento = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Caixa'
    
    def __str__(self):
        return self.tipo
