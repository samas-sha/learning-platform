"""
Enrollment model: student enrolls in a course.
"""
from django.db import models
from django.conf import settings
from courses.models import Course


class Enrollment(models.Model):
    """Student enrollment in a course (free or paid)."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['user', 'course']]
        ordering = ['-enrolled_at']

    def __str__(self):
        return f'{self.user.username} – {self.course.title}'
