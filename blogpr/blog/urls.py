from django.urls import path
from .views import task_list, task_detail, hello, index

urlpatterns = [
    # map our view to this url
    path('', task_list, name='list'),
    path('detail/<int:id>/', task_detail, name='detail'),
    path('hello/', hello),
    path('index/', index, name='index')
    # map our view to this url
]

