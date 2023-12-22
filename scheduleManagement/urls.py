from django.urls import path
from . import views

urlpatterns = [
  path('', views.MainRequestHandler.as_view(), name='home'),
  
  path('disciplina/<int:disciplina_id>', views.DisciplinaRequestHandler.as_view(), name='disciplina_details'),
  
  path('add-course/', views.CourseAddRequestHandler.as_view(), name='add_course'),
  path('details/<int:curso_id>', views.DetailsRequestHandler.as_view(), name='curso_details'),
  path('edit-course/<int:curso_id>', views.CourseEditRquestHandler.as_view(), name='edit_course'),
]