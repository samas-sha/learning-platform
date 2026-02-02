"""
Progress tracking: lesson completion per user.
"""
from django.db import models
from django.conf import settings
from lessons.models import Lesson


class LessonProgress(models.Model):
    """Tracks when a user completed a lesson."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lesson_progress'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='progress_records'
    )
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['user', 'lesson']]
        verbose_name = 'Lesson progress'
        verbose_name_plural = 'Lesson progress'

    def __str__(self):
        return f'{self.user.username} – {self.lesson.title}'
