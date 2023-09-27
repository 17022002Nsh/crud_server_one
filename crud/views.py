from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    tasks = Todo.objects.all()
    
    context = {
        'tasks': tasks
    }
    
    return render(request, 'index.html', context)

def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        todo =Todo(
            title=title
        )
        todo.save()
        
        return redirect("home")
    return render(request, 'create.html')

def edit_todo(request, pk):
    vazifa = Todo.objects.get(id=pk)
    
    
    
    if request.method == "POST":
        text = request.POST.get("title")
        vazifa.title = text
        vazifa.save()
        return redirect("home")
    return render(request, 'edit.html')

def delete_todo(request, pk):
    text = Todo.objects.get(id=pk)
    text.delete()
    return redirect("home")
    
    
