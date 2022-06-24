# import the standard django model from built-in library
from django.db import models


# Create your models here.
# declare a new model with the name TodoApp
class TodoApp(models.Model):
    # fileds of the model
    title = models.CharField(max_length=200)
    description = models.TextField()
    # renames the instances of model with their title name
    def __str__(self):
        return self.title
