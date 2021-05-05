from django.db import models
from django.contrib.auth.models import User
# Create your models here.

options = [
    ('Rightwing','rightwing'),
    ('Leftwing', 'leftwing'),
    ('Defensemen', 'defensemen'),
    ('Center', 'center'),
    ('Goaltender', 'goaltender'),
]

class BudgetEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player = models.CharField(max_length=128)
    position = models.CharField(max_length=20, choices=options)
    points = models.PositiveIntegerField()
    prediction = models.PositiveIntegerField()
