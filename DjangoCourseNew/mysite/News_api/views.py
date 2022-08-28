from django.contrib.auth import authenticate, login,logout
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.db import IntegrityError

# Create your views here.

from django.shortcuts import render
from newsapi import NewsApiClient
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def home(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    top = newsapi.get_top_headlines(category='general')

    l=top['articles']
    desc=[]
    news=[]
    img=[]
    url=[]
    author=[]

    for i in range(len(l)):
        f=l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
        author.append(f['author'])
    
    mylist= zip(news,desc,img,url,author)

    return render(request,'news/home.html',{'mylist':mylist})


def bbcNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    top = newsapi.get_top_headlines(sources ='bbc-news')

    articles = top['articles']

    desc = []
    news = []
    img = []
    url=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        author.append(myarticles['author'])


    mylist = zip(news, desc, img,url,author)
    
    return render(request,'news/bbc.html',{'mylist':mylist})

def footballTransfer(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    top = newsapi.get_top_headlines(category='sports',q='football transfer')
    

    articles = top['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])

    mylist = zip(news, desc, img, url,date,author)
    return render (request,'news/footballtransfer.html',{'mylist':mylist})

    
def abcNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    top = newsapi.get_top_headlines(sources ='abc-news')
    

    articles = top['articles']

    desc = []
    news = []
    img = []
    url=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        author.append(myarticles['author'])


    mylist = zip(news, desc, img,url,author)
    
    return render(request,'news/abc.html',{'mylist':mylist})



    
def sportsNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    topSports = newsapi.get_top_headlines(category="sports")
    

    articles = topSports['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])


    mylist = zip(news, desc, img, url,date,author)
    
    return render(request,'news/sports.html',{'mylist':mylist})



def techNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    topTech = newsapi.get_top_headlines(category="technology")

    articles = topTech['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])


    mylist = zip(news, desc, img, url,date,author)
    
    return render(request,'news/sports.html',{'mylist':mylist})

def businessNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    topBusiness = newsapi.get_top_headlines(category="business")

    articles = topBusiness['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])


    mylist = zip(news, desc, img, url,date,author)
    
    return render(request,'news/sports.html',{'mylist':mylist})


def entertainmentNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    topEntertainment = newsapi.get_top_headlines(category="entertainment")

    articles = topEntertainment['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])


    mylist = zip(news, desc, img, url,date,author)
    
    return render(request,'news/sports.html',{'mylist':mylist})


def healthNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    topHealth = newsapi.get_top_headlines(category="health")

    articles = topHealth['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])


    mylist = zip(news, desc, img, url,date,author)
    
    return render(request,'news/sports.html',{'mylist':mylist})


def specialNews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    specialNews = newsapi.get_top_headlines(category='general',q='corona')

    articles = specialNews['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])



    mylist = zip(news, desc, img, url,date,author)
    return render(request,'news/specialnews.html',{'mylist':mylist})



def liverpoolnews(request):
    newsapi = NewsApiClient(api_key ='be58d0b353d54967b1ed4fe91c74ef27')
    top = newsapi.get_top_headlines(category='sports',q='liverpool')
    

    articles = top['articles']

    desc = []
    news = []
    img = []
    url=[]
    date=[]
    author=[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        date.append(myarticles['publishedAt'])
        author.append(myarticles['author'])

    mylist = zip(news, desc, img, url,date,author)
    return render (request,'news/liverpoolclubnews.html',{'mylist':mylist})

def usersignup(request):
    if request.method=='GET':
        return render(request,'news/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except:
                return(request,'news/signup.html',{'form':UserCreationForm(),'error':"This Username is taken, Try another name"})
        else:
            return render(request,'news/signup.html',{'form':UserCreationForm(),'error':'Password is not matching'})


def userlogin(request):
    if request.method=='GET':
        return render(request,'news/login.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'news/login.html',{'form':AuthenticationForm(),'error':"Username or password is invalid try again"})
        else:
            login(request,user)
            return redirect('home')


def userlogout(request):
    logout(request)
    return redirect('home')