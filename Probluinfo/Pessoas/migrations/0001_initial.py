# Generated by Django 4.0.5 on 2022-07-18 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('nm_completo', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(blank=True, max_length=50, unique=True)),
                ('dt_nascimento', models.DateField(max_length=10)),
                ('celular', models.CharField(blank=True, max_length=11, unique=True)),
                ('fone_res', models.CharField(blank=True, max_length=10, unique=True)),
                ('nm_resp', models.CharField(blank=True, max_length=100)),
                ('login', models.CharField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=50)),
                ('contato', models.CharField(blank=True, max_length=100)),
                ('perfil', models.CharField(choices=[('1', 'Administrador'), ('2', 'Instrutor'), ('3', 'Vendedor')], max_length=1)),
                ('dt_alteracao', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Pessoas',
            },
        ),
    ]
