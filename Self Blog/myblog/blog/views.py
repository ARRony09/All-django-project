from .models import PostNew
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def blogList(request):
    allposts=PostNew.objects.all()
    params={'allposts': allposts}
    return render(request,'blog/blog_list.html',params)


def blogDetails(request,slug):
    post_details=PostNew.objects.filter(slug=slug).first()
    params={'post':post_details}
    return render(request,'blog/blog_details.html',params)
