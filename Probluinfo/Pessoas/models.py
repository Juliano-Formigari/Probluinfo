from django.db import models
# Create your models here.

class Pessoas(models.Model):
    Aluno = 1
    Instrutor = 2
    Vendedor = 3
    Administrador = 4

    PERFIS_CHOICES = (
        (Aluno,'Aluno'),
        (Instrutor,'Instrutor'),
        (Vendedor,'Vendedor'),
        (Administrador,'Administrador')
    )

    nm_completo = models.CharField(max_length=100, blank=False) # Nome completo
    cpf = models.CharField(max_length=14, blank=False, unique=True) # CPF somente numeros
    email = models.EmailField(max_length=50, blank=True, unique=True) # Email com validação
    dt_nascimento = models.DateField(max_length=10, blank=False) # Somente numeros, pois no banco salva com '/'
    celular = models.CharField(max_length=15, blank=True, unique=True) # Somente numeros
    fone_res = models.CharField(max_length=14, blank=True, unique=True) # Telefone resindencial, somente numeros
    nm_resp = models.CharField(max_length=100, blank=True) # Nome da mãe, ou responsável caso não tenha, e seja menor de idade
    login = models.CharField(max_length=50, blank=False, unique=True)
    senha = models.CharField(max_length=50, blank=False)
    perfil = models.CharField(max_length=1,choices=PERFIS_CHOICES, blank=False)
    dt_alteracao = models.DateField(auto_now=True) # Data de registro de alteração do cadastro

    class Meta:
        db_table = 'Pessoas'

    def __str__(self):
        return self.nm_completo
    