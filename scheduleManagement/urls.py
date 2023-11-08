from django.urls import path
from . import views

urlpatterns = [
  path('', views.main_request_handler.as_view(), name='main'),
  path('details/<int:curso_id>', views.details_request_handler.as_view(), name='curso_details'),
  path('disciplina/<int:disciplina_id>', views.disciplina_request_handler.as_view(), name='disciplina_details')
]