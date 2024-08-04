from django.contrib import admin
from .models import Post

# registering the model task
class PostModel(admin.ModelAdmin):
    #list_display = how you want to display in the admin
    list_display = ['title', 'author', 'content', 'date_created']
    search_fields = ['author', 'title']

# Register your models here.
admin.site.register(Post, PostModel)
