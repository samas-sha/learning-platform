"""
Lesson model linked to courses.
"""
from django.db import models
from courses.models import Course


class Lesson(models.Model):
    """Lesson within a course (video URL, notes, order)."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, help_text='YouTube or other video URL')
    content = models.TextField(blank=True, help_text='Text notes / content')
    order = models.PositiveIntegerField(default=0, help_text='Display order within course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['course', 'order', 'id']
        unique_together = [['course', 'order']]

    def __str__(self):
        return f'{self.course.title} – {self.title}'
