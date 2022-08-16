# Generated by Django 4.0.4 on 2022-08-13 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0006_alter_pessoas_fone_res'),
        ('Financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='id_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pessoas.pessoas'),
        ),
        migrations.AlterField(
            model_name='caixa',
            name='tipo',
            field=models.CharField(choices=[(1, 'Entrada'), (2, 'Saída')], max_length=1),
        ),
    ]