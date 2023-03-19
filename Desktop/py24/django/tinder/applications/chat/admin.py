from django.contrib import admin

from applications.chat.models import Chat, Message

admin.site.register(Chat)
admin.site.register(Message)
