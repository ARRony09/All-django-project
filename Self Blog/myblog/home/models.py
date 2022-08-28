from django.db import models

# Create your models here.

class Contact(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    desc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Message from " + self.username+" at " +(self.time).strftime('%Y-%m-%d %H:%M')
    
