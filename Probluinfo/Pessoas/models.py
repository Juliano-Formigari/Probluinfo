from django.db import models

# Create your models here.
class Aluno(models.Model):
    nm_completo = models.CharField(max_length=100, blank=False) # Nome completo
    cpf = models.CharField(max_length=11, unique=True, blank=False, primary_key=True) # CPF somente numeros
    email = models.EmailField(max_length=50, blank=True, unique=True) # Email com validação
    dt_nascimento = models.DateField(max_length=10, blank=False) # Somente numeros, pois no banco salva com '/'
    celular = models.CharField(max_length=11, blank=True, unique=True) # Somente numeros
    fone_res = models.CharField(max_length=10, blank=True, unique=True) # Telefone resindencial, somente numeros
    nm_resp = models.CharField(max_length=100, blank=True) # Nome da mãe, ou responsável caso não tenha, e seja menor de idade
    dt_alteracao = models.DateField(auto_now=True) # Data de registro de alteração do cadastro


    class Meta:
        db_table = 'Aluno'

    def __str__(self):
        return self.nm_completo

# Nova tabela abaixo
        