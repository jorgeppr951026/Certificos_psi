# Generated by Django 3.2.11 on 2022-12-20 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0011_certifico_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certifico',
            name='estado',
        ),
    ]
