from django.contrib import admin
from todo_list.models import TodoItem


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = "id", "name", "is_done"
    list_display_links = "id", "name"
    list_filter = ["is_done"]
