from django.views.generic import ListView
from django.shortcuts import render

from ..models import Curso, Disciplina, Horario


class CourseListRequestHandler(ListView):
    model = Curso

    def get(self, request):
        return render(
            request,
            "list-object.html",
            {"objects": Curso.objects.all(), "object_type": "Course"},
        )


class DisciplineListRequestHandler(ListView):
    model = Curso

    def get(self, request):
        return render(
            request,
            "list-object.html",
            {"objects": Disciplina.objects.all(), "object_type": "Discipline"},
        )
    

class ScheduleListRequestHandler(ListView):
    model = Horario

    def get(self, request):
        return render(
            request,
            "list-object.html",
            {"objects": Horario.objects.all(), "object_type": "Schedule"},
        )