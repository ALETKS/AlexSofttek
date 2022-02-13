from django.db import models

# Create your models here.

class OrderClass(models.Model):
    order_number = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
