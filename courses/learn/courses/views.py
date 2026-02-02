from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def course_detail(request, pk):
	course = get_object_or_404(Course, pk=pk)
	return render(request, 'course_detail.html', {'course': course})

from .models import Enrollment

@login_required
def enroll(request, pk):
	course = get_object_or_404(Course, pk=pk)
	enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
	if created:
		messages.success(request, f'You have enrolled in {course.title}!')
	else:
		messages.info(request, f'You are already enrolled in {course.title}.')
	return redirect('course_detail', pk=pk)
from django.shortcuts import render

# Create your views here.
