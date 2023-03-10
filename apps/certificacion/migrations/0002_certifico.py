# Generated by Django 3.2.11 on 2022-12-18 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250, unique=True, verbose_name='Codigo')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('asesorador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.asesorador', verbose_name='Asesorador')),
                ('certificador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.certificador', verbose_name='Certifcador')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.cliente', verbose_name='Cliente')),
                ('psi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificacion.psi', verbose_name='Plan de Seguridad')),
            ],
            options={
                'verbose_name': 'Certifico',
                'verbose_name_plural': 'Certificos',
            },
        ),
    ]
