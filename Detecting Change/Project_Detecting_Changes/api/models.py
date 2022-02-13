from django.db import models

# Create your models here.

class WeatherClass(models.Model):
    date=models.CharField(max_length=10)
    was_rainy=models.CharField(max_length=10)