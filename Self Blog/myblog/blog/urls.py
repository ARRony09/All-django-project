from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.blogList,name='blogList'),
    path("<str:slug>",views.blogDetails,name='blogDetails')
]