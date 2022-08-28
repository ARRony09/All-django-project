from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('createurl', views.createurl,name="createurl"),
    path('urlcreated', views.urls,name="urls"),
]
