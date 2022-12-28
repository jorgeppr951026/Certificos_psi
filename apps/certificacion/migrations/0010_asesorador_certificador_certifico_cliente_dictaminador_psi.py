# Generated by Django 3.2.11 on 2022-12-20 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certificacion', '0009_auto_20221219_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesorador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('cargo', models.CharField(choices=[('Especialista', 'Especialista'), ('Director(a)', 'Director(a)')], default='Especialista', max_length=250, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Asesorador',
                'verbose_name_plural': 'Asesoradores',
            },
        ),
        migrations.CreateModel(
            name='Certificador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('cargo', models.CharField(choices=[('Especialista', 'Especialista'), ('Director(a)', 'Director(a)')], default='Especialista', max_length=250, verbose_name='Cargo')),
                ('tomo', models.CharField(max_length=250, verbose_name='Tomo')),
                ('folio', models.CharField(max_length=250, verbose_name='Folio')),
                ('numero', models.CharField(default=' ', max_length=250, verbose_name='Numero')),
            ],
            options={
                'verbose_name': 'Certificador',
                'verbose_name_plural': 'Certificadors',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('organismo', models.CharField(default=' ', max_length=250, verbose_name='Organismo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Dictaminador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('cargo', models.CharField(default='Especialista', max_length=250, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Dictaminador',
                'verbose_name_plural': 'Dictaminadores',
            },
        ),
        migrations.CreateModel(
            name='PSI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('estado', models.BooleanField(choices=[(False, 'Pendiente'), (True, 'Certificado')], default=False)),
                ('asesorador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.asesorador', verbose_name='Asesorador')),
                ('certificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.certificador', verbose_name='Certifcador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.cliente', verbose_name='Cliente')),
                ('dictaminador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.dictaminador', verbose_name='Certifcador')),
            ],
            options={
                'verbose_name': 'PSI',
                'verbose_name_plural': 'PSIs',
            },
        ),
        migrations.CreateModel(
            name='Certifico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250, unique=True, verbose_name='Codigo')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('psi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.psi', verbose_name='Plan de Seguridad')),
            ],
            options={
                'verbose_name': 'Certifico',
                'verbose_name_plural': 'Certificos',
            },
        ),
    ]
