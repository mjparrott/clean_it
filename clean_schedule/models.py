from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)

class Group(models.Model):
  name = models.CharField(max_length=100)
  users = models.ManyToManyField(User)

class TaskType(models.Model):
  type = models.CharField(max_length = 100)
  weight = models.IntegerField(max_value = 5, min_value = 1)
  freq = models.IntegerField(max_value = 3, min_value = 1)

class Task(models.Model):
  user = models.ForeignKey('User')
  done = models.BooleanField()

