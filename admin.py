from django.contrib import admin
from .models import Task_model

class Task_admin(admin.ModelAdmin):
    list_display=('task','is_active','created_at','updated_to')

admin.site.register(Task_model,Task_admin)