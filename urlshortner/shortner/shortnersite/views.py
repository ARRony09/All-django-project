import uuid
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Shortner

# Create your views here.
def index(request):
    return render(request,"index.html")

def create(request):
    if request.method == "POST":
        link=request.POST["link"]
        uid=str(uuid.uuid4())[0:5]
        url=Shortner(link=link,uuid=uid)
        url.save()
        return HttpResponse(uid)

def go(request,pk):
    url_details=Shortner.objects.get(uuid=pk)
    return redirect("https://"+url_details.link)