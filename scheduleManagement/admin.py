from django.contrib import admin
from .models import Disciplina, Curso, Horario

for model in [
    Disciplina,
    Curso,
    Horario,
]:
    admin.site.register(model)
