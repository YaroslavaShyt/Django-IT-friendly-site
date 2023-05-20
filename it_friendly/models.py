from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint




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
    beginning = models.CharField(max_length=8)
    studying_direction = models.ForeignKey(StudyingDirection, on_delete=models.CASCADE, to_field='id')
    teacher = models.ManyToManyField(Worker)
    students = models.ManyToManyField(User)


class StudyingStudent(models.Model):
    username_student = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    id_course = models.ForeignKey(Studying, on_delete=models.CASCADE, to_field='id')

    class Meta:
        constraints = [
            UniqueConstraint(fields=['username_student', 'id_course'], name='unique_study_student')
        ]
