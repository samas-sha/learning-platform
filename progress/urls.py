from django.urls import path
from . import views

app_name = 'progress'

urlpatterns = [
    path('lesson/<slug:course_slug>/<int:lesson_id>/', views.lesson_view, name='lesson_view'),
    path('complete/<int:lesson_id>/', views.mark_lesson_complete, name='mark_complete'),
]
