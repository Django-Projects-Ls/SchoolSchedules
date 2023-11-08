from django.views import View
from django.shortcuts import render
from .models import Curso, Disciplina

# Create your views here.
class main_request_handler(View):
  def get(self, request):
    return render(request, 'index.html', {'cursos': Curso.objects.all()})

class details_request_handler(View):
  def get(self, request, curso_id):
    return render(request, 'details.html', {'curso': Curso.objects.get(id=curso_id)})

class disciplina_request_handler(View):
  def get(self, request, disciplina_id):
    return render(request, 'disciplina.html', {'disciplina' : Disciplina.objects.get(id=disciplina_id)})