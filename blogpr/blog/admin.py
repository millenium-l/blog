from django.contrib import admin
from .models import Task

# registering the model task
class TaskModel(admin.ModelAdmin):
    #list_display = how you want to display in the admin
    list_display = ['title', 'author', 'content', 'date_created']
    search_fields = ['author', 'title']

# Register your models here.
admin.site.register(Task, TaskModel)
