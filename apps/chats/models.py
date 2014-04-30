from django.db import models
from django.core.validators import MinLengthValidator

from autoslug import AutoSlugField

from ..users.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_by = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name="room_members")
    slug = AutoSlugField(populate_from='name')
    key = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(6)],
        help_text=('6-15 characters. Letters, digits and @/./+/-/_ only.'))

    def __unicode__(self):
        return self.name
