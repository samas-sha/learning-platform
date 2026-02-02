"""
Course list and detail views. Admin management is via Django admin.
"""
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course, Category


def get_published_courses():
    return Course.objects.filter(status=Course.Status.PUBLISHED).select_related('category')


class CourseListView(ListView):
    """List all published courses with optional category filter."""
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 12

    def get_queryset(self):
        qs = get_published_courses()
        category_slug = self.request.GET.get('category')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context


class CourseDetailView(DetailView):
    """Course detail with curriculum (lessons) preview."""
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Course.objects.filter(status=Course.Status.PUBLISHED).prefetch_related('lessons').select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lessons.all().order_by('order')
        context['user_enrolled'] = False
        if self.request.user.is_authenticated:
            from enrollments.models import Enrollment
            context['user_enrolled'] = Enrollment.objects.filter(
                user=self.request.user, course=self.object
            ).exists()
        return context
