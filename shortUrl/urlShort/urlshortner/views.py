from django.shortcuts import redirect, render
import random
import string
from .models import Url
import uuid
# Create your views here.

def index(request):
    return render(request,"index.html")

def createurl(request):
    if request.method == 'POST':
        inputurl=request.POST['url']
        #slug=''.join(random.choice(string.ascii_letters)
                      #  for x in range(10))
        slug=str(uuid.uuid4())[:5]
        data_url = Url(new_url=inputurl,slug=slug)
        data_url.save()
        return redirect('/')

def urls(request):
    allUrls=Url.objects.all()
    params={"allUrls":allUrls}
    return render(request,"urls.html",params)

