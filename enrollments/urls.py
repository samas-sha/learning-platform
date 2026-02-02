from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('my-learning/', views.my_learning, name='my_learning'),
    path('enroll/<slug:slug>/', views.enroll_course, name='enroll'),
    path('confirmation/<slug:slug>/', views.enrollment_confirmation, name='enrollment_confirmation'),
]
