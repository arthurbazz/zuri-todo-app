from django.urls import path
from .views import TodoAppCreateView, TodoAppListView, TodoAppDetailView, TodoAppUpdateView, TodoAppDeleteView


urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list.html', TodoAppListView.as_view(), name='list'),
    path('detail/<pk>', TodoAppDetailView.as_view(), name='detail'),
    path('update/<pk>', TodoAppUpdateView.as_view(), name='update'),
    path('delete/<pk>', TodoAppDeleteView.as_view()),
]
