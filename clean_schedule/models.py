from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class CleanUser(models.Model):
  user = models.OneToOneField(User)
  group = models.ForeignKey('Group', null=True)

class Group(models.Model):
  name = models.CharField(max_length=100)

class TaskType(models.Model):
  type = models.CharField(max_length = 100)
  weight = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
  freq = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(3)])

class Task(models.Model):
  user = models.ForeignKey('CleanUser')
  done = models.BooleanField(default = 'False')
  datetime = models.DateTimeField()
