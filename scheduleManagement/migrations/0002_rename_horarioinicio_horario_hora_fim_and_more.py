# Generated by Django 4.2.7 on 2023-12-24 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horario',
            old_name='horarioInicio',
            new_name='hora_fim',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='horarioTermino',
            new_name='hora_inicio',
        ),
    ]