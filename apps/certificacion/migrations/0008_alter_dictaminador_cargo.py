# Generated by Django 3.2.11 on 2022-12-20 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0007_dictaminador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictaminador',
            name='cargo',
            field=models.CharField(default='Especialista', max_length=250, verbose_name='Cargo'),
        ),
    ]
