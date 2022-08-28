from django.urls import path,include
from News_api import views



urlpatterns = [
    path('',views.home,name='home'),
    path('bbc/',views.bbcNews,name='bbcNews'),
    path('football/',views.footballTransfer,name='footballTransfer'),
    path('abc/',views.abcNews,name='abcNews'),
    path('sports/',views.sportsNews,name='sportsNews'),
    path('business/',views.businessNews,name='businessNews'),
    path('entertainment/',views.entertainmentNews,name='entertainmentNews'),
    path('health/',views.healthNews,name='healthNews'),
    path('technology/',views.techNews,name='techNews'),
    path('specialnews/',views.specialNews,name='specialNews'),
    path('liverpoolnews/',views.liverpoolnews,name='liverpoolnews'),
    path('signup/',views.usersignup,name='usersignup'),
    path('login/',views.userlogin,name='userlogin'),
    path('logout/',views.userlogout,name='userlogout'),
]
