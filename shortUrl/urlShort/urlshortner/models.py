from django.db import models

# Create your models here.

class Url(models.Model):
    new_url=models.CharField(max_length=1000)
    slug=models.CharField(max_length=15)