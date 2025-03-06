from django.urls import path,include

from . import views

urlpatterns = [
    path('todo/',views.Todo_views,name="todo"),
    #path('todo/',views.AddTask_views,name="todo"),
    path('task/delete/<int:pk>',views.Delete_task,name="delete_task"),
    path('task/edit/<int:pk>',views.Edit_task,name="edit_task"),
    path('task/complite/<int:pk>',views.Completed_task,name="complited_task"),
    path('task/undone/<int:pk>',views.Uncompleted_task,name="uncomplited_task"),
]

