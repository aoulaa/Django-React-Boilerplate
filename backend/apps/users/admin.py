from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name',
              'last_name',
              'email',
              'username',
              'is_active',
              'is_superuser')

    readonly_fields = ['username']
