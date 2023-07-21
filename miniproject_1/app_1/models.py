from django.db import models

# Create your models here.
class Java(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=30)
    book = models.CharField(max_length=30)
    rate = models.FloatField()
    year = models.IntegerField()
    language = models.CharField(max_length=35)

class Python(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=30)
    book = models.CharField(max_length=30)
    rate = models.FloatField()
    year = models.IntegerField()
    language = models.CharField(max_length=35)