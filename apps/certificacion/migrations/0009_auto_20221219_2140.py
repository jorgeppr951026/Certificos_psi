# Generated by Django 3.2.11 on 2022-12-20 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0008_alter_dictaminador_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certifico',
            name='psi',
        ),
        migrations.DeleteModel(
            name='Dictaminador',
        ),
        migrations.RemoveField(
            model_name='psi',
            name='asesorador',
        ),
        migrations.RemoveField(
            model_name='psi',
            name='certificador',
        ),
        migrations.RemoveField(
            model_name='psi',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Asesorador',
        ),
        migrations.DeleteModel(
            name='Certificador',
        ),
        migrations.DeleteModel(
            name='Certifico',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='PSI',
        ),
    ]
