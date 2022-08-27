from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    band = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    rating=models.FloatField(null=True, default=3)
