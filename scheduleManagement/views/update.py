from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from ..models import Curso, Disciplina, Horario


class UserUpdateRequestHandler(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'form.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'user'
        return context


class CourseUpdateRequestHandler(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ["nome", "codigo", "disciplinas", "horario"]
    template_name = "form.html"

    def get_success_url(self):
        return reverse_lazy("detail_course", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "course"
        return context


class DisciplineUpdateRequestHandler(LoginRequiredMixin, UpdateView):
    model = Disciplina
    fields = ["nome", "codigo"]
    template_name = "form.html"

    def get_success_url(self):
        return reverse_lazy("detail_discipline", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "discipline"
        return context


class ScheduleUpdateRequestHandler(LoginRequiredMixin, UpdateView):
    model = Horario
    fields = ["dia", "hora_inicio", "hora_fim"]
    template_name = "form.html"

    def get_success_url(self):
        return reverse_lazy("detail_schedule", kwargs={"slug": self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_type"] = "schedule"
        return context
