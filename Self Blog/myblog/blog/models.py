from django.db import models

# Create your models here.

class PostNew(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200, unique=True)
    content=models.TextField()
    image=models.ImageField(upload_to='blog/image',default='')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

