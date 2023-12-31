from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy

from ..models import Curso, Disciplina, Horario
from ..forms import CustomUserCreationForm


# This is a Django view file for creating various entities like User, Course, Discipline, and Schedule.


class UserCreateRequestHandler(CreateView):
    # This class handles the creation of a new User.
    form_class = CustomUserCreationForm
    template_name = "registration/sign_up.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # This method is called when the form is valid.
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)  # Call the parent class's form_valid method.


class CourseCreateRequestHandler(LoginRequiredMixin, CreateView):
    # This class handles the creation of a new Course.
    model = Curso
    fields = [
        "nome",
        "codigo",
        "disciplinas",
        "horario",
    ]
    template_name = "form.html"
    success_url = reverse_lazy("list_courses")


class DisciplineCreateRequestHandler(LoginRequiredMixin, CreateView):
    # This class handles the creation of a new Discipline.
    model = Disciplina
    fields = [
        "nome",
        "codigo",
        "horario",
    ]
    template_name = "form.html"
    success_url = reverse_lazy("list_disciplines")


class ScheduleCreateRequestHandler(LoginRequiredMixin, CreateView):
    # This class handles the creation of a new Schedule.
    model = Horario  # The model to be used for creating a new Schedule.
    fields = [
        "dia",
        "hora_inicio",
        "hora_fim",
    ]
    template_name = "form.html"
    success_url = reverse_lazy("list_schedules")
