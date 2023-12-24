from django.contrib import admin
from .models import Disciplina, Curso, Horario

# Register your models here.
for model in [Disciplina, Curso, Horario]:
  admin.site.register(model)
