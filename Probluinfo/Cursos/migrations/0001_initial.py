# Generated by Django 4.0.4 on 2022-07-29 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_curso', models.CharField(max_length=50, unique=True)),
                ('carga_horaria', models.DecimalField(decimal_places=0, max_digits=3)),
                ('vl_curso', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
            options={
                'db_table': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Matriculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inicio', models.DateField()),
                ('dt_fim', models.DateField()),
                ('qtd_dias', models.DecimalField(decimal_places=0, max_digits=3)),
                ('qtd_horas', models.DecimalField(decimal_places=0, max_digits=3)),
                ('periodo', models.CharField(choices=[(1, 'Matutino'), (2, 'Verpertino'), (3, 'Noturno')], max_length=1)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cursos.cursos')),
                ('id_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pessoas', to='Pessoas.pessoas')),
            ],
            options={
                'db_table': 'Matriculas',
            },
        ),
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_sala', models.CharField(max_length=50, unique=True)),
                ('capacidade', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
            options={
                'db_table': 'Salas',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_1', models.DecimalField(decimal_places=2, max_digits=3)),
                ('nota_2', models.DecimalField(decimal_places=2, max_digits=3)),
                ('nota_3', models.DecimalField(decimal_places=2, max_digits=3)),
                ('nota_4', models.DecimalField(decimal_places=2, max_digits=3)),
                ('media', models.DecimalField(decimal_places=2, max_digits=3)),
                ('id_matricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cursos.matriculas')),
            ],
            options={
                'db_table': 'Notas',
            },
        ),
        migrations.AddField(
            model_name='matriculas',
            name='id_sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cursos.salas'),
        ),
    ]
