from django.db import models

from ..users.models import User
from ..chats.models import ChatRoom


class Message(models.Model):
    user = models.ForeignKey(User)
    room = models.ForeignKey(ChatRoom)
    body = models.CharField(max_length=140)

    def __unicode__(self):
        return self.body
