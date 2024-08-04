from django.db import models
"""
Imports: The models module is imported from django.db, which is essential for defining Django models.

Task Model: Defines a model named Task which represents a task in the application.

title: A character field for the task's title, with a maximum length of 100 characters.
content: A text field for the task's content, with a maximum length of 500 characters.
author: A character field for the author's name, limited to 50 characters.
date_created: A date-time field that automatically records when the task was created.
__str__ Method: Provides a string representation of the Task instance. Note: The status attribute in the __str__ method should be defined in the model; otherwise, it will cause an error.

"""

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"title: {self.title}, \ncontent: {self.content}, \nauthor: {self.author}"
