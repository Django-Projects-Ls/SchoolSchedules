# Generated by Django 4.2.7 on 2023-12-26 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleManagement', '0003_curso_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
