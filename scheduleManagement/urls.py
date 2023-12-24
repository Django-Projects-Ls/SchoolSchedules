from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
  path('', TemplateView.as_view(template_name='home.html'), name='home'),

  path('list-courses/', views.CourseListRequestHandler.as_view(), name='list_courses'),
  path('list-courses/create/', views.CourseCreateRequestHandler.as_view(), name='create_course'),
  path('list-courses/<int:pk>', views.CourseDetailsRequestHandler.as_view(), name='detail_course'),
  path('list-courses/edit/<int:pk>', views.CourseUpdateRequestHandler.as_view(), name='edit_course'),
  path('list-courses/delete/<int:pk>', views.CourseDeleteRequestHandler.as_view(), name='delete_course'),
  
  path('list-disciplines/', views.DisciplineListRequestHandler.as_view(), name='list_disciplines'),
  path('list-disciplines/create/', views.DisciplineCreateRequestHandler.as_view(), name='create_discipline'),
  path('list-disciplines/<int:pk>', views.DisciplineDetailsRequestHandler.as_view(), name='detail_discipline'),
  path('list-disciplines/edit/<int:pk>', views.DisciplineUpdateRequestHandler.as_view(), name='edit_discipline'),
  path('list-disciplines/delete/<int:pk>', views.DisciplineDeleteRequestHandler.as_view(), name='delete_discipline'),

  path('list-schedules/', views.ScheduleListRequestHandler.as_view(), name='list_schedules'),
  path('list-schedules/create/', views.ScheduleCreateRequestHandler.as_view(), name='create_schedule'),
  path('list-schedules/<int:pk>', views.ScheduleDetailsRequestHandler.as_view(), name='detail_schedule'),
  path('list-schedules/edit/<int:pk>', views.ScheduleUpdateRequestHandler.as_view(), name='edit_schedule'),
  path('list-schedules/delete/<int:pk>', views.ScheduleDeleteRequestHandler.as_view(), name='delete_schedule'),
]