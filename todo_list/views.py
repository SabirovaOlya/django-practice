from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import TodoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_tasks = TodoItem.objects.all()
    return render(
        request,
        template_name='todo_list/index.html',
        context={'todo_tasks': todo_tasks}
    )


class TodoListIndexView(TemplateView):
    template_name = 'todo_list/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_tasks"] = TodoItem.objects.all()
        return context


class TodoListView(ListView):
    template_name = "todo_list/index.html"
    queryset = TodoItem.objects.all()[:2]


class TodoListAllView(ListView):
    template_name = "todo_list/list.html"
    model = TodoItem


class TodoListDetailView(DetailView):
    model = TodoItem
