from django.forms import ModelForm
from random import choices
from django.db import models
from .models import Cursos,Periodos,Salas,Matriculas,Notas
 


# Create your models here.
class FormCursos(ModelForm):
    model = Cursos
    fields = ['id','nm_curso','carga_horaria','vl_curso']
    db_table = 'Cursos'          

class FormSalas(ModelForm):
    model = Salas
    fields = ['id','nm_sala','capacidade']  
    db_table = 'Salas'

class FormPeriodos(ModelForm):
    model = Periodos
    fields = ['id','descricao'] 
    db_table = 'Periodos'

class FormMatriculas(ModelForm):
    model = Matriculas
    fields = ['id','id_vendedor','dt_inicio','dt_fim','td_dias','qtd_horas','id_aluno','id_curso','id_periodo','id_sala','id_instrutor','id_perfil']   
    db_table = 'Matriculas'

class FormNotas(ModelForm):
    model = Notas
    fields = ['id','id_matricula','nota_1','nota_2','nota_3','nota_4','media']
    db_table = 'Notas'
