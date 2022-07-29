from django.db import models
from Pessoas.models import Pessoas

# Create your models here.
class Cursos(models.Model):
    nm_curso = models.CharField(max_length=50, blank=False, unique=True)
    carga_horaria = models.DecimalField(max_digits=3, decimal_places=0,blank=False)
    vl_curso = models.DecimalField(max_digits=5, decimal_places=3, blank=False)

    class Meta:
        db_table = 'Cursos'

    def __str__(self):
        return self.nm_curso
            
class Salas(models.Model):
    nm_sala = models.CharField(max_length=50, blank=False, unique=True)
    capacidade = models.DecimalField(max_digits=3, decimal_places=0 ,blank=False)

    class Meta:
        db_table = 'Salas'
    
    def __str__(self):
        return self.nm_sala

class Matriculas(models.Model):
    Turnos = (
    ('1' , 'Matutino'),
    ('2' , 'Verpertino'),
    ('3', 'Noturno'),
    )
    id_vendedor = models.ForeignKey(Pessoas, related_name='vendedor',on_delete=models.PROTECT)
    dt_inicio = models.DateField(blank=False)
    dt_fim = models.DateField(blank=False)
    qtd_dias = models.DecimalField(max_digits=3,decimal_places=0,blank=False)
    qtd_horas = models.DecimalField(max_digits=3,decimal_places=0,blank=False)
    id_aluno = models.ForeignKey(Pessoas,related_name='aluno', on_delete=models.PROTECT)
    id_curso = models.ForeignKey(Cursos,on_delete=models.PROTECT)
    periodo = models.CharField(max_length=1,choices=Turnos,blank=False)
    id_sala = models.ForeignKey(Salas,on_delete=models.PROTECT)
    id_instrutor = models.ForeignKey(Pessoas,on_delete=models.PROTECT)
    id_perfil = models.ForeignKey(Pessoas,related_name='cargos',on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'Matriculas'
    
    def __str__(self):
        return self.id_aluno

class Notas(models.Model):
    id_matricula = models.ForeignKey(Matriculas,blank=False,on_delete=models.PROTECT)
    nota_1 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    nota_2 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    nota_3 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    nota_4 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    media = models.DecimalField(max_digits=3,decimal_places=2)

    class Meta:
        db_table = 'Notas'

    def __str__(self):
        return self.id_matricula
    


    