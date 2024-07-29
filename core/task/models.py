from django.db import models
from django.contrib.auth.models import User

class UserTask(models.Model):
    task_choices = (
        ('j', 'plus'),
        ('m', 'minus'),
        ('z', 'multiple'),
        ('t', 'division')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.CharField(max_length=255, unique=True)
    task_type = models.CharField(max_length=50, choices=task_choices)  # e.g., 'add_numbers'
    status = models.CharField(max_length=50)  # e.g., 'PENDING'
    result = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)