from django.contrib import admin

from applications.chat.models import Chat, Block

admin.site.register(Chat)
admin.site.register(Block)
