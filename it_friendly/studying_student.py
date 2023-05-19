from django.db import models


class StudyingStudent:
    username_student = models.CharField(max_length=70)
    id_course = models.CharField(max_length=100)
