from django.shortcuts import redirect, render
from .models import Todolist

# Create your views here.

def index(request):
    if request.method=="POST":
        title=request.POST["title"]
        todo=Todolist(title=title)
        todo.save()
    
    view_todo=Todolist.objects.all()
    params={"view_todo":view_todo}

    return render(request,"index.html",params)

def delete(request,pk):
    alltodos=Todolist.objects.get(sno=pk)
    alltodos.delete()
    return redirect("/")