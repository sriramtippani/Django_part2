from django.db import models

# Create your models here.

class Detail1Model(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    preffered_name = models.CharField(max_length=64)
    title_name = models.CharField(max_length=64)
    email = models.EmailField()
    contact_no = models.BigIntegerField()
    contact_ext = models.BigIntegerField()
    join_date = models.DateField()
    join_date_format = models.CharField(max_length=64)
    team = models.CharField(max_length=64)
    job_title = models.CharField(max_length=64)
