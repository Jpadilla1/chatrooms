from django.db import models

from autoslug import AutoSlugField

from ..users.models import User


class Room(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_by = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name="room_members")
    slug = AutoSlugField(populate_from='name')
    key = models.CharField(max_length=15,)

    def __unicode__(self):
        return self.name
