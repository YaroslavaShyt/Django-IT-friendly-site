from django.db import models


class Studying(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    price = models.IntegerField()
    level = models.CharField(max_length=70)
    time = models.CharField(max_length=30)
    details = models.CharField(max_length=300)
    participants = models.CharField(max_length=50)
    programs_settings = models.CharField(max_length=500)
    beginning = models.DateTimeField()

