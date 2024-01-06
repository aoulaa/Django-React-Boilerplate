from django.db import models

from config.settings import AUTH_USER_MODEL

from core.models import BaseModel
from todo.querysets.todo import TodoQuerySet


class Todo(BaseModel):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(AUTH_USER_MODEL, models.CASCADE)
    objects = TodoQuerySet.as_manager()

    def __str__(self):
        return self.title
