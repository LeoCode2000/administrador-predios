# Generated by Django 3.2.7 on 2021-11-10 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_predio_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predio',
            name='propietarios',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='predios',
        ),
    ]