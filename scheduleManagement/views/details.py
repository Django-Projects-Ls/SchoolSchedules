from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import Curso, Disciplina, Horario
from ..extras import get_field_values


class CourseDetailsRequestHandler(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "object-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_field_values(context["object"])
        context["object_type"] = "course"
        return context


class DisciplineDetailsRequestHandler(LoginRequiredMixin, DetailView):
    model = Disciplina
    template_name = "object-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_field_values(context["object"])
        context["object_type"] = "discipline"
        return context


class ScheduleDetailsRequestHandler(LoginRequiredMixin, DetailView):
    model = Horario
    template_name = "object-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_field_values(context["object"])
        context["object_type"] = "schedule"
        return context
