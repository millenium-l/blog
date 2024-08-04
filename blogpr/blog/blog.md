# 1.Creating and Managing Models

## a: Importing a Model
First, let's define our model in models.py:

    from django.db import models

    class Post(models.Model):
        title = models.CharField(max_length=200)   # Title of the post
        content = models.TextField()               # Content of the post
        author = models.CharField(max_length=100)  # Author of the post
        date_created = models.DateTimeField(auto_now_add=True)  # Creation date

        def __str__(self):
            return self.title

## b: Making Migrations 
Open your terminal and run the following command to create migration files:

     ./manage.py makemigrations

    

## c: Applying Migrations 
Apply the migrations to update your database schema:

        ./manage.py migrate

## d. Adding Data Using the Shell 
Use the Django shell to add data to your database:

        ./manage.py shell

### In the shell:

from your_app.models import Post

        ##### Create a new post
    post1 = Post(title='Alchemist', content='This is a the alchemist book', author='paulo cuelo')
    post1.save()

e. Creating a Superuser
To manage your project via the Django admin interface, create a superuser:

            ./manage.py createsuperuser
Follow the prompts to enter a username and password.

f. Running the Development Server
Start the Django development server:

        ./manage.py runserver

g. Accessing the Admin Interface
Open your web browser and navigate to:

        http://localhost:8000/admin
        
Log in using the superuser credentials you created.

h. Registering Models in Admin
In admin.py, import and register your model:

        from django.contrib import admin
from .models import Post

    admin.site.register(Post)


# 2. Creating Templates
a. Directory Structure
Create the following directories for your templates:

        blog/templates/blog/detail.html
        blog/templates/blog/list.html


## b. Template Files
detail.html: Used to display details of a single post.

list.html: Used to list all posts.

3. Setting Up Views
In views.py, define the views to handle requests:
        from django.shortcuts import render, get_object_or_404
from .models import Post

        def post_list(request):
            posts = Post.objects.all()
            return render(request, 'blog/list.html', {'posts': posts})

        def post_detail(request, id):
            post = get_object_or_404(Post, id=id)
            return render(request, 'blog/detail.html', {'post': post})

4. Writing Template Content
Add HTML content to list.html and detail.html:

list.html:
            
        <!DOCTYPE html>
        <html>
            <head>
                    <title>Post List</title>
            </head>
                <body>
                    <h1>Post List</h1>
                        <ul>
                            {% for post in posts %}
                            <li><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></li>
                            {% endfor %}
                        </ul>
                </body>
        </html>


## detail.html:
            <!DOCTYPE html>
            <html>
                <head>
                    <title>{{ post.title }}</title>
                </head>
                    <body>
                        <h1>{{ post.title }}</h1>
                        <p>{{ post.content }}</p>
                        <p><em>By {{ post.author }}</em></p>
                        <a href="{% url 'post_list' %}">Back to list</a>
                    </body>
            </html>


## 5. Configuring URL Patterns
In urls.py, add paths to link the views:

        from django.urls import path
        from .views import post_list, post_detail

    urlpatterns = [
    path('', post_list, name='post_list'),
    path('detail/<int:id>/', post_detail, name='post_detail'),
    ]


## 6. Viewing in the Browser
To view the details of a post, navigate to:

        http://localhost:8000/detail/1/
        




