# Generated by Django 3.1.3 on 2020-11-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(blank=True, max_length=19, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(blank=True, max_length=50, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=19, verbose_name='Telefone Fixo'),
        ),
    ]