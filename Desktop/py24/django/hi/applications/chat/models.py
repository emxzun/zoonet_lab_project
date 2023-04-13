from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model


User = get_user_model()

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, default=True)
    content = models.TextField(default='')
    image = models.ImageField(upload_to='chat_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    block_users = models.ManyToManyField(User, related_name='blocked_chats', default=set)

    class Meta:
        ordering = ('updated_at',)







