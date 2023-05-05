from django.db import models
from django.contrib.auth.models import User


class StudyingType(models.Model):
    title = models.CharField(max_length=50)


class StudyingDirection(models.Model):
    title = models.CharField(max_length=70)


class Worker(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=400)
    duties = models.CharField(max_length=200)


class FAQ(models.Model):
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)


class Studying(models.Model):
    type = models.ForeignKey(StudyingType, on_delete=models.CASCADE, to_field='id')
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    price = models.IntegerField()
    level = models.CharField(max_length=70)
    time = models.CharField(max_length=30)
    details = models.CharField(max_length=300)
    participants = models.CharField(max_length=50)
    programs_settings = models.CharField(max_length=500)
    beginning = models.DateTimeField()
    studying_direction = models.ForeignKey(StudyingDirection, on_delete=models.CASCADE, to_field='id')
    teacher = models.ManyToManyField(Worker)
    students = models.ManyToManyField(User)


