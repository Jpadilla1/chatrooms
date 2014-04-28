from django.db import models

from ..users.models import User
from ..chats.models import ChatRoom


class Message(models.Model):
    created_by = models.ForeignKey(User)
    room = models.ForeignKey(ChatRoom)
    created_at = models.DateTimeField(auto_now=False)
    body = models.CharField(max_length=140,
                            help_text='Max characters is 140.')

    def __unicode__(self):
        return self.body
