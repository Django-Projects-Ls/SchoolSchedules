from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_request_handler, name='main'),
  path('details/<int:curso_id>', views.details_request_handler, name='curso_details'),
  path('disciplina/<int:disciplina_id>', views.disciplina_request_handler, name='disciplina_details')
]