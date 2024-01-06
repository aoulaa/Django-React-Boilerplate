from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'is_active', 'user')
    readonly_fields = ['id', ]
