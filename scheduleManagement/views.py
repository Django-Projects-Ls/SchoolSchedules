from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .extras import get_field_values
from .models import Curso, Disciplina, Horario

class CourseListRequestHandler(ListView):
  model = Curso

  def get(self, request):
    return render(request, 'list-object.html', {'objects': Curso.objects.all(), 'object_type': 'Course'})

class CourseCreateRequestHandler(CreateView):
  model = Curso
  fields = ['nome', 'codigo', 'disciplinas', 'horario']
  template_name = 'form.html'
  success_url = reverse_lazy('list_courses')

class CourseDetailsRequestHandler(DetailView):
  model = Curso
  template_name = 'object-details.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object'] = get_field_values(context['object'])
    context['object_type'] = 'course'
    return context

class CourseUpdateRequestHandler(UpdateView):
  model = Curso
  fields = ['nome', 'codigo', 'disciplinas', 'horario']
  template_name = 'form.html'
  
  def get_success_url(self):
    return reverse_lazy('detail_course', kwargs={'pk': self.object.pk})

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_type'] = 'course'
    return context

class CourseDeleteRequestHandler(DeleteView):
  model = Curso
  template_name = 'confirm-delete.html'
  success_url = reverse_lazy('list_courses')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_type'] = 'course'
    return context

class DisciplineListRequestHandler(ListView):
  model = Curso

  def get(self, request):
    return render(request, 'list-object.html', {'objects': Disciplina.objects.all(), 'object_type': 'Discipline'})

class DisciplineCreateRequestHandler(CreateView):
  model = Disciplina
  fields = ['nome', 'codigo', 'horario']
  template_name = 'form.html'
  success_url = reverse_lazy('list_disciplines')

class DisciplineDetailsRequestHandler(DetailView):
  model = Disciplina
  template_name = 'object-details.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object'] = get_field_values(context['object'])
    context['object_type'] = 'discipline'
    return context

class DisciplineUpdateRequestHandler(UpdateView):
  model = Disciplina
  fields = ['nome', 'codigo']
  template_name = 'form.html'
  
  def get_success_url(self):
    return reverse_lazy('detail_discipline', kwargs={'pk': self.object.pk})

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_type'] = 'discipline'
    return context
  
class DisciplineDeleteRequestHandler(DeleteView):
  model = Disciplina
  template_name = 'confirm-delete.html'
  success_url = reverse_lazy('list_disciplines')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_type'] = 'discipline'
    return context
  
class ScheduleListRequestHandler(ListView):
  model = Horario

  def get(self, request):
    return render(request, 'list-object.html', {'objects': Horario.objects.all(), 'object_type': 'Schedule'})
  
class ScheduleCreateRequestHandler(CreateView):
  model = Horario
  fields = ['dia', 'hora_inicio', 'hora_fim']
  template_name = 'form.html'
  success_url = reverse_lazy('list_schedules')

class ScheduleDetailsRequestHandler(DetailView):
  model = Horario
  template_name = 'object-details.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object'] = get_field_values(context['object'])
    context['object_type'] = 'schedule'
    return context
  
class ScheduleUpdateRequestHandler(UpdateView):
  model = Horario
  fields = ['dia', 'hora_inicio', 'hora_fim']
  template_name = 'form.html'
  
  def get_success_url(self):
    return reverse_lazy('detail_schedule', kwargs={'pk': self.object.pk})

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_type'] = 'schedule'
    return context

class ScheduleDeleteRequestHandler(DeleteView):
  model = Horario
  template_name = 'confirm-delete.html'
  success_url = reverse_lazy('list_schedules')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_type'] = 'schedule'
    return context
