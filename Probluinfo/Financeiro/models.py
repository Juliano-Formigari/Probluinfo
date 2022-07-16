from django.db import models
from django.forms import CharField

# Create your models here.
class Caixa(models.Model):
    class Tipos(models.IntegerChoices):
        Entrada = '1'
        Saída = '2'
    tipo = models.IntegerField(choices=Tipos.choices)
    descricao = models.CharField(max_length=50, blank=False)
    valor = models.FloatField(MaxValueValidator=10, blank=True)

    class Meta:
        db_table = 'Caixa'
    
    def __str__(self):
        return self.tipo
