# Generated by Django 4.0.4 on 2022-08-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0005_alter_pessoas_fone_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='fone_res',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
