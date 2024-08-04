from django.urls import path
from .views import post_list, post_detail, hello, index

urlpatterns = [
    # map our view to this url
    path('', post_list, name='list'),
    path('detail/<int:id>/', post_detail, name='detail'),
    path('hello/', hello),
    path('index/', index, name='index')
    # map our view to this url
]

