from django.db import models

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
    descricao = models.CharField(max_length=20, blank=False, unique=True, primary_key=True)

    class Meta:
        db_table = 'Periodos'

    def __str__(self):
        return self.descricao