from django.contrib import admin
from imagekit.admin import AdminThumbnail

from applications.announcement.models import Announcement, ImageAnnouncement


class ImageAnnouncementInline(admin.StackedInline):
    model = ImageAnnouncement

class AnnouncementAdmin(admin.ModelAdmin):
    inlines = [ImageAnnouncementInline]
    list_filter = ('category', 'location')

admin.site.register(Announcement, AnnouncementAdmin)



