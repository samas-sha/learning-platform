"""
Enrollment: enroll in course, my learning dashboard.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from courses.models import Course
from .models import Enrollment
from progress.models import LessonProgress


@login_required
def my_learning(request):
    """Student dashboard: enrolled courses and progress overview."""
    enrollments = (
        Enrollment.objects
        .filter(user=request.user)
        .select_related('course')
        .order_by('-enrolled_at')
    )
    # Progress per course
    course_progress = []
    for enr in enrollments:
        course = enr.course
        total = course.lessons.count()
        completed = LessonProgress.objects.filter(
            user=request.user,
            lesson__course=course
        ).count()
        pct = int((completed / total * 100)) if total else 0
        # Last lesson (for "resume")
        last_lesson = None
        if completed < total and total > 0:
            if completed > 0:
                last_prog = (
                    LessonProgress.objects
                    .filter(user=request.user, lesson__course=course)
                    .select_related('lesson')
                    .order_by('-completed_at')
                    .first()
                )
                if last_prog:
                    next_lessons = course.lessons.filter(order__gt=last_prog.lesson.order).order_by('order')
                    last_lesson = next_lessons.first() if next_lessons.exists() else None
                else:
                    last_lesson = None
            else:
                last_lesson = course.lessons.order_by('order').first()
        else:
            last_lesson = None  # All complete or no lessons – show "View Course"
        course_progress.append({
            'enrollment': enr,
            'course': course,
            'completed': completed,
            'total': total,
            'percentage': pct,
            'resume_lesson': last_lesson,
        })
    return render(request, 'enrollments/my_learning.html', {'course_progress': course_progress})


@login_required
def enroll_course(request, slug):
    """Enroll current user in a course (free)."""
    course = get_object_or_404(Course, slug=slug, status=Course.Status.PUBLISHED)
    if Enrollment.objects.filter(user=request.user, course=course).exists():
        messages.info(request, 'You are already enrolled in this course.')
        return redirect('enrollments:my_learning')
    Enrollment.objects.create(user=request.user, course=course)
    messages.success(request, f'You have been enrolled in "{course.title}".')
    return redirect('enrollments:enrollment_confirmation', slug=slug)


@login_required
def enrollment_confirmation(request, slug):
    """Enrollment confirmation page."""
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    first_lesson = course.lessons.order_by('order').first()
    return render(request, 'enrollments/enrollment_confirmation.html', {
        'course': course,
        'enrollment': enrollment,
        'first_lesson': first_lesson,
    })
