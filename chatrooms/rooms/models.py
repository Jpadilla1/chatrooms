from django.db import models

from ..users.models import User


class Room(models.Model):
    title = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, related_name='owner')
    created_at = models.DateTimeField(auto_now_add=False)
    members = models.ManyToManyField(User)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title
