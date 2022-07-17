from django.db import models
from django.forms import CharField
from .models import Pessoas

# Create your models here.
class Caixa(models.Model):
    class Tipos(models.IntegerChoices):
        Entrada = '1'
        Saída = '2'
    tipo = models.IntegerField(choices=Tipos.choices)
    id_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, blank=False)
    valor = models.FloatField(MaxValueValidator=10, blank=True)
    dt_lancamento = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Caixa'
    
    def __str__(self):
        return self.tipo
