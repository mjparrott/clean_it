from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
  name = models.CharField(max_length=100)
  users = models.ManyToManyField(User)

class TaskType(models.Model):
  type = models.CharField(max_length = 100)
  weight = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
  freq = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(3)])

class Task(models.Model):
  user = models.ForeignKey(User)
  done = models.BooleanField(default = 'False')
  datetime = models.DateTimeField()
