# Generated by Django 3.2.11 on 2022-12-19 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0003_remove_cliente_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='organismo',
            field=models.CharField(default=' ', max_length=250, verbose_name='Organismo'),
        ),
    ]
