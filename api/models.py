from django.db import models
from datetime import date
# Create your models here.
class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    interval = models.IntegerField(default=1)
    last_learned = models.DateField(default=date(1990,1,1))
class Settings(models.Model):
    study_time = models.TimeField()
    questions_per_day = models.IntegerField(default=20)