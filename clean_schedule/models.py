from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)

class Group(models.Model):
  name = models.CharField(max_length=100)
  users = models.ManyToManyField(User)

