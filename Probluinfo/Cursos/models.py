from random import choices
from django.db import models
from Pessoas.models import Pessoas,Perfis
from Cursos.models import Cursos,Periodos,Salas


# Create your models here.
class Cursos(models.Model):
    nm_curso = models.CharField(max_length=50, blank=False, unique=True, primary_key=True)
    carga_horaria = models.IntegerField(max_length=3 ,blank=False)
    vl_curso = models.FloatField(max_length=8, blank=False)

    class Meta:
        db_table = 'Cursos'

    def __str__(self):
        return self.nm_curso
            

class Salas(models.Model):
    nm_sala = models.CharField(max_length=50, blank=False, unique=True, primary_key=True)
    capacidade = models.IntegerField(max_length=3, blank=False)

    class Meta:
        db_table = 'Salas'
    
    def __str__(self):
        return self.nm_sala

class Periodos(models.Model):
    class Turnos(models.IntegerChoices):
        Matutino = '1'
        Verpertino = '2'
        Noturno = '3'

    descricao = models.IntegerChoices(choices=Turnos.choices)

    class Meta:
        db_table = 'Periodos'

    def __str__(self):
        return self.descricao

class Matriculas(models.Model):
    id_vendedor = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    dt_inicio = models.DateField(blank=False)
    dt_fim = models.DateField(blank=False)
    qtd_dias = models.IntegerField(blank=False)
    qtd_horas = models.IntegerField(blank=False)
    id_aluno = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    id_periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    id_instrutor = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    id_perfil = models.ForeignKey(Perfis, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Matriculas'
    
    def __str__(self):
        return self.id_aluno

class Notas(models.Model):
    id_matricula = models.ForeignKey(Matriculas, blank=False)
    nota_1 = models.FloatField(max_length=4, blank=False)
    nota_2 = models.FloatField(max_length=4, blank=False)
    nota_3 = models.FloatField(max_length=4, blank=False)
    nota_4 = models.FloatField(max_length=4, blank=False)
    media = models.FloatField(max_length=4)

    class Meta:
        db_table = 'Notas'

    def __str__(self):
        return self.id_matricula
    


    