from django.db import models

# Create your models here.

class DeliveryAddress(models.Model):
    address = models.CharField(max_length = 200)
    