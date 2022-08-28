from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,"customer/home.html")

def about(request):
    return render(request,'customer/about.html') 
