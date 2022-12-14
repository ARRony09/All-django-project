from django.db import models
from django.http import request


# Create your models here.
CATEGORY_CHOICES=(
    ('A','ACTION'),
    ('D','DRAMA'),
    ('C','COMEDY'),
    ('R','ROMANCE'),
)
LANGUAGE_CHOICES=(
    ('EN','ENGLISH'),
    ('GR','GERMAN'),
    ('HN','HINDI'),
)

STATUS_CHOICES=(
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to="movies")
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=1)
    language=models.CharField(choices=LANGUAGE_CHOICES,max_length=2)
    status=models.CharField(choices=STATUS_CHOICES,max_length=2)
    year_of_production = models.CharField(max_length=20)
    views_count=models.IntegerField(default=0)

    def __str__(self):
        return self.title
