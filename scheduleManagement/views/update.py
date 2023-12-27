from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from ..models import Curso, Disciplina, Horario

class CourseUpdateRequestHandler(UpdateView):
    model = Curso
    fields = ["nome", "codigo", "disciplinas", "horario"]
    template_name = "form.html"

    def get_success_url(self):
        return reverse_lazy("detail_course", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "course"
        return context


class DisciplineUpdateRequestHandler(UpdateView):
    model = Disciplina
    fields = ["nome", "codigo"]
    template_name = "form.html"

    def get_success_url(self):
        return reverse_lazy("detail_discipline", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "discipline"
        return context


class ScheduleUpdateRequestHandler(UpdateView):
    model = Horario
    fields = ["dia", "hora_inicio", "hora_fim"]
    template_name = "form.html"

    def get_success_url(self):
        return reverse_lazy("detail_schedule", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "schedule"
        return context