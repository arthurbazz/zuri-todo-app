from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TodoApp

# Create your views here.
class TodoAppCreateView(CreateView):
    # specify the model for createview
    model = TodoApp

    # specify fields to be displayed
    fields = [
        'title',
        'description'
    ]
    template_name = 'home.html'
    success_url = 'list.html'

class TodoAppListView(ListView):
    # specifiy the model for the list view
    model = TodoApp
    template_name = 'list.html'

class TodoAppDetailView(DetailView):
    # specify the model to use
    model = TodoApp
    template_name = 'detail.html'   

class TodoAppUpdateView(UpdateView):
    # Specify the model to use
    model = TodoApp
    # specify fields to be displayed
    fields = [
        'title',
        'description'
    ]
    template_name = 'update.html'
    success_url = '/'

class TodoAppDeleteView(DeleteView):
    # specify the model you want to use
    model = TodoApp
    template_name = 'delete.html'
    success_url = '/'