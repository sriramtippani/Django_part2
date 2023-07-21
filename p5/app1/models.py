from django.db import models

# Create your models here.
class Hjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Bjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Pjob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    eligibility = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
