from django.urls import path
from django.views.generic import TemplateView
from .views import TodoListIndexView, TodoListView, TodoListAllView, TodoListDetailView

app_name = 'todo_list'
urlpatterns = [
    path('', TodoListView.as_view(), name='index'),
    path('list/', TodoListAllView.as_view(), name='list'),
    path('<int:pk>/', TodoListDetailView.as_view(), name='detail'),
]
