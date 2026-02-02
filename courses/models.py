"""
Course model for the learning platform.
"""
from django.db import models
from django.conf import settings


class Category(models.Model):
    """Course category (e.g. Programming, Design)."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Course(models.Model):
    """Course with details for admin management."""
    class Level(models.TextChoices):
        BEGINNER = 'beginner', 'Beginner'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        ADVANCED = 'advanced', 'Advanced'

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    level = models.CharField(max_length=20, choices=Level.choices, default=Level.BEGINNER)
    duration = models.CharField(max_length=50, blank=True, help_text='e.g. 4 hours, 6 weeks')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='instructed_courses'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def lesson_count(self):
        return self.lessons.count()

    def total_duration_display(self):
        return self.duration or 'Self-paced'
