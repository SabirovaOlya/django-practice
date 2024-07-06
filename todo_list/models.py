from django.db import models
from django.db.models import Model


class TodoItem(Model):
    class Meta:
        verbose_name = 'TODO Item'
        ordering = ("id", )

    name = models.CharField(max_length=120)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
