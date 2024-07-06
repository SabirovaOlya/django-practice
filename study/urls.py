from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('todo/', include('todo_list.urls'))
]

