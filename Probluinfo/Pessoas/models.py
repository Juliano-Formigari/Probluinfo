from django.db import models
from Pessoas.models import Perfil


# Create your models here.
class Pessoas(models.Model):

    nm_completo = models.CharField(max_length=100, blank=False) # Nome completo
    cpf = models.CharField(max_length=14, unique=True, blank=False, primary_key=True) # CPF somente numeros
    email = models.EmailField(max_length=50, blank=True, unique=True) # Email com validação
    dt_nascimento = models.DateField(max_length=10, blank=False) # Somente numeros, pois no banco salva com '/'
    celular = models.CharField(max_length=11, blank=True, unique=True) # Somente numeros
    fone_res = models.CharField(max_length=10, blank=True, unique=True) # Telefone resindencial, somente numeros
    nm_resp = models.CharField(max_length=100, blank=True) # Nome da mãe, ou responsável caso não tenha, e seja menor de idade
    dt_alteracao = models.DateField(auto_now=True) # Data de registro de alteração do cadastro
    contato = models.CharField(max_length=100, blank=True) # Nome da mãe, ou responsável caso não tenha, e seja menor de idade
    login = models.CharField(max_length=50, blank=False, unique=True)
    senha = models.CharField(max_length=50, blank=False)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    dt_alteracao = models.DateField(auto_now=True) # Data de registro de alteração do cadastro

    class Meta:
        db_table = 'Pessoas'


    def __str__(self):
        return self.nm_completo

# Nova tabela abaixo
        

class Perfis(models.Model):
    ds_perfil = models.CharField(max_length=30, blank=False, unique=True)

    class Meta:
        db_table = 'Perfis'
    
    def __str__(self):
        return self.ds_perfil
        