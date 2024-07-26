from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('This is our basic todo app')

# returning html pages
def index(request):
    context = {
        'name': 'kimari'
    }
    return render(request, 'blog/index.html', context)