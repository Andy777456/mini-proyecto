from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
