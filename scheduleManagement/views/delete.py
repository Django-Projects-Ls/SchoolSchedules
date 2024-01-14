from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from ..models import Curso, Disciplina, Horario


class UserDeleteRequestHandler(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "confirm-delete.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "user"
        return context


class CourseDeleteRequestHandler(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = "confirm-delete.html"
    success_url = reverse_lazy("list_courses")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "course"
        return context


class DisciplineDeleteRequestHandler(LoginRequiredMixin, DeleteView):
    model = Disciplina
    template_name = "confirm-delete.html"
    success_url = reverse_lazy("list_disciplines")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "discipline"
        return context


class ScheduleDeleteRequestHandler(LoginRequiredMixin, DeleteView):
    model = Horario
    template_name = "confirm-delete.html"
    success_url = reverse_lazy("list_schedules")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "schedule"
        return context
