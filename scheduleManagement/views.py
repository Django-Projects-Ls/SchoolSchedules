from django.views import View
from django.shortcuts import render, redirect
from .models import Curso, Disciplina
from .forms import CursoForm

# Create your views here.
class MainRequestHandler(View):
  def get(self, request):
    return render(request, 'index.html', {'cursos': Curso.objects.all()})

class DetailsRequestHandler(View):
  def get(self, request, curso_id):
    return render(request, 'details.html', {'curso': Curso.objects.get(id=curso_id)})

class DisciplinaRequestHandler(View):
  def get(self, request, disciplina_id):
    return render(request, 'disciplina.html', {'disciplina' : Disciplina.objects.get(id=disciplina_id)})

class CourseAddRequestHandler(View):
  def get(self, request):
    return render(request, 'course.html', {'form': CursoForm()})
  
  def post(self, request):
    form = CursoForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('/')
    
    return render(request, 'course.html', {'form': form})
  
class CourseEditRquestHandler(View):
  def get(self, request, curso_id):
    return render(request, 'course.html', {'form': CursoForm(instance=Curso.objects.get(id=curso_id))})
  
  def post(self, request, curso_id):
    form = CursoForm(request.POST, instance=Curso.objects.get(id=curso_id))

    if form.is_valid():
      form.save()
      return redirect('/')
    
    return render(request, 'course.html', {'form': form})
  
  
