"""
Progress: mark lesson complete, view lesson (restricted to enrolled students).
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST
from courses.models import Course
from lessons.models import Lesson
from enrollments.models import Enrollment
from .models import LessonProgress


def _user_can_access_lesson(user, lesson):
    """Only enrolled students (or staff) can access lesson content."""
    if user.is_staff:
        return True
    return Enrollment.objects.filter(user=user, course=lesson.course).exists()


@login_required
def lesson_view(request, course_slug, lesson_id):
    """View a single lesson (video + notes). Restricted to enrolled students."""
    course = get_object_or_404(Course, slug=course_slug, status=Course.Status.PUBLISHED)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    if not _user_can_access_lesson(request.user, lesson):
        return HttpResponseForbidden('You must enroll in this course to view lessons.')
    lessons_list = list(course.lessons.order_by('order'))
    try:
        current_index = next(i for i, l in enumerate(lessons_list) if l.id == lesson.id)
    except StopIteration:
        current_index = 0
    prev_lesson = lessons_list[current_index - 1] if current_index > 0 else None
    next_lesson = lessons_list[current_index + 1] if current_index < len(lessons_list) - 1 else None
    completed_ids = set(
        LessonProgress.objects.filter(user=request.user, lesson__course=course).values_list('lesson_id', flat=True)
    )
    return render(request, 'progress/lesson_view.html', {
        'course': course,
        'lesson': lesson,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
        'lessons_list': lessons_list,
        'completed_ids': completed_ids,
    })


@login_required
@require_POST
def mark_lesson_complete(request, lesson_id):
    """Mark a lesson as completed (idempotent)."""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if not _user_can_access_lesson(request.user, lesson):
        return HttpResponseForbidden()
    LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/'))
    return redirect(next_url)
