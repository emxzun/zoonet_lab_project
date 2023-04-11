from django.contrib import admin
from applications.announcement.models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_filter = ('category', 'location')

