from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from ..models import Curso, Disciplina, Horario


class CourseCreateRequestHandler(CreateView):
    model = Curso
    fields = ["nome", "codigo", "disciplinas", "horario"]
    template_name = "form.html"
    success_url = reverse_lazy("list_courses")


class DisciplineCreateRequestHandler(CreateView):
    model = Disciplina
    fields = ["nome", "codigo", "horario"]
    template_name = "form.html"
    success_url = reverse_lazy("list_disciplines")

class ScheduleCreateRequestHandler(CreateView):
    model = Horario
    fields = ["dia", "hora_inicio", "hora_fim"]
    template_name = "form.html"
    success_url = reverse_lazy("list_schedules")