from datetime import date
from django.db import models
from positions.models import Position

# Create your models here.
class Employee(models.Model):
    lastname = models.CharField(max_length=100)
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    title = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    class Meta():
        ordering = ['lastname']
