from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

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
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/list.html', {'posts':posts})

# providing details in the d
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post':post})