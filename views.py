from django.shortcuts import render,get_object_or_404,redirect

from .models import Task_model

# Create your views here.
def Todo_views(request):
    tasks=Task_model.objects.filter(is_active=False)

    print(tasks)


    contax={
        "tasks":tasks
    }
    return render(request,'todo_app/todo.html',contax)