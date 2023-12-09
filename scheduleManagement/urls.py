from django.urls import path
from . import views
from .models import Curso

urlpatterns = [
  path('', views.MainRequestHandler.as_view(), name='main'),
  path('details/<int:curso_id>', views.DetailsRequestHandler.as_view(), name='curso_details'),
  path('disciplina/<int:disciplina_id>', views.DisciplinaRequestHandler.as_view(), name='disciplina_details'),
  path('add-course/', views.CourseAddRequestHandler.as_view(), name='add_course'),
  path('edit-course/<int:curso_id>', views.CourseEditRquestHandler.as_view(), name='edit_course'),
]