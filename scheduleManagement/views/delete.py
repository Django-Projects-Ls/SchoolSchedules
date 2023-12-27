from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from ..models import Curso, Disciplina, Horario


class CourseDeleteRequestHandler(DeleteView):
    model = Curso
    template_name = "confirm-delete.html"
    success_url = reverse_lazy("list_courses")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "course"
        return context


class DisciplineDeleteRequestHandler(DeleteView):
    model = Disciplina
    template_name = "confirm-delete.html"
    success_url = reverse_lazy("list_disciplines")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "discipline"
        return context


class ScheduleDeleteRequestHandler(DeleteView):
    model = Horario
    template_name = "confirm-delete.html"
    success_url = reverse_lazy("list_schedules")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "schedule"
        return context
