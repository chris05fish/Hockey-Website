from django.db import models
from django.contrib.auth.models import User
# Create your models here.

options = [
    ('Win', 'win'),
    ('Loss', 'loss'),
]

class TasksEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opposing = models.CharField(max_length=128)
    win = models.CharField(max_length=20, choices=options, default='win')
