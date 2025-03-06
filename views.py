from django.shortcuts import render,get_object_or_404,redirect

from .models import Task_model

# Create your views here.
def Todo_views(request):
    tasks=Task_model.objects.filter(is_active=False).order_by('-created_at')  # if the models attributs - that means its reverse

    complited_tasks=Task_model.objects.filter(is_active=True)

    if request.method=="POST":
        new_task=Task_model(task=request.POST.get('addfontendTask'))
        new_task.save()

        return redirect('todo') 


    contax={
        "tasks":tasks,
        "complited_tasks":complited_tasks
    }
    return render(request,'todo_app/todo.html',contax)


# def AddTask_views(request):
#     if request.method=="POST":
#         new_task=Task_model(task=request.POST.get('addfontendTask'))
#         new_task.save()

#         return redirect('todo')

#     return render(request,'todo_app/todo.html')


def Delete_task(request,pk):
    task=get_object_or_404(Task_model,pk=pk)
    task.delete()
    return redirect('todo')



def Edit_task(request,pk):
    task=get_object_or_404(Task_model,pk=pk)

    if request.method=="POST":
        task.task=request.POST.get('addfontendTask')

        task.save()
        return redirect("todo")


    contax={
        "task":task
    }
    return render(request,'todo_app/todo.html',contax)

def Completed_task(request,pk):
    complited=get_object_or_404(Task_model,pk=pk)
    complited.is_active=True
    complited.save()
    return redirect("todo")

def Uncompleted_task(request,pk):
    uncomplited=get_object_or_404(Task_model,pk=pk)
    uncomplited.is_active=False
    uncomplited.save()

    return redirect('todo')