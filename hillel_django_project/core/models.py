from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)


class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
