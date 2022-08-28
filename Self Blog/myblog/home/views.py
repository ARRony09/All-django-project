from home.models import Contact
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from blog.models import PostNew
# from newsapi import NewsApiClient


# Create your views here.

def home(request):
    post_details=PostNew.objects.filter(author='AR Rony').first()
    allposts=PostNew.objects.all()
    params={'post':post_details,'allposts':allposts}
    return render(request,'home/home.html',params)


def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        desc=request.POST['desc']
        contact=Contact(username=username,email=email,desc=desc)
        contact.save()
        messages.success(request,"Your message has been succesfully submitted")
    return render(request,'home/contact.html')

def donate(request):
    return render(request,'home/donate.html')

