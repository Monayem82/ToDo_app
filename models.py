from django.db import models

class Task_model(models.Model):
    task=models.CharField(max_length=200,null=False)
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_to=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.task}"
