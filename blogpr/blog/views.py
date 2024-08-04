from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def hello(request):
    return HttpResponse('This is our basic todo app')

# returning html pages
def index(request):
    context = {
        'name': 'kimari'
    }
    return render(request, 'blog/index.html', context)

# listing elements in the list html tag
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'blog/list.html', {'tasks':tasks})

# providing details in the d
def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'blog/detail.html', {'task':task})