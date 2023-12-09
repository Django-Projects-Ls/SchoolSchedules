from django.contrib import admin
from .models import Disciplina, Curso, Horario

# Register your models here.
admin.site.register(Disciplina)
admin.site.register(Curso)
admin.site.register(Horario)