"""
Custom User model with Admin and Student roles.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user with role-based access (Admin / Student)."""
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STUDENT = 'student', 'Student'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT
    )

    def is_admin_user(self):
        return self.role == self.Role.ADMIN or self.is_staff

    def is_student_user(self):
        return self.role == self.Role.STUDENT

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
