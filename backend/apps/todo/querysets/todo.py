from django.db.models import Q

from core.querysets.base_queryset import BaseQuerySet


class TodoQuerySet(BaseQuerySet):
    def list(self, search=None, user=None):
        query = self.filter(Q(title__icontains=search) | Q(description__icontains=search)) if search else self
        query = query.filter(user=user) if user else query
        query = query.order_by('-is_active', '-created_at')
        return query
