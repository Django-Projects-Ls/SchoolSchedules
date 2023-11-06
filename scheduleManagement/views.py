from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Disciplina

# Create your views here.
def main_request_handler(request):
  return render(request, 'index.html', {'cursos': Curso.objects.all()})

def details_request_handler(request, curso_id):
  return render(request, 'details.html', {'curso': Curso.objects.get(id=curso_id)})

def disciplina_request_handler(request, disciplina_id):
  return render(request, 'disciplina.html', {'disciplina' : Disciplina.objects.get(id=disciplina_id)})