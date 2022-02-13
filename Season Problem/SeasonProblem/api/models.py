from django.db import models

# Create your models here.

class SeasonClass(models.Model):
    ORD_ID=models.CharField(max_length=100)
    ORD_DT=models.DateField()