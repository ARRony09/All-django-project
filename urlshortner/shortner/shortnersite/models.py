from django.db import models

# Create your models here.

class Shortner(models.Model):
    sno=models.AutoField(primary_key=True)
    link=models.CharField(max_length=1000)
    uuid=models.CharField(max_length=10)