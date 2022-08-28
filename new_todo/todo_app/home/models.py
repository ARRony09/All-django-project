from django.db import models
from matplotlib.pyplot import title

# Create your models here.

class Todolist(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=2000)
    
    def __str__(self):
        return self.title
