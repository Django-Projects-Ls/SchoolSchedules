from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy

from ..models import Curso, Disciplina, Horario
from ..forms import CustomUserCreationForm


class UserCreateRequestHandler(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CourseCreateRequestHandler(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ["nome", "codigo", "disciplinas", "horario"]
    template_name = "form.html"
    success_url = reverse_lazy("list_courses")


class DisciplineCreateRequestHandler(LoginRequiredMixin, CreateView):
    model = Disciplina
    fields = ["nome", "codigo", "horario"]
    template_name = "form.html"
    success_url = reverse_lazy("list_disciplines")


class ScheduleCreateRequestHandler(LoginRequiredMixin,CreateView):
    model = Horario
    fields = ["dia", "hora_inicio", "hora_fim"]
    template_name = "form.html"
    success_url = reverse_lazy("list_schedules")
