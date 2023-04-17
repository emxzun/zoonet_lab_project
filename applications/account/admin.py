from django.contrib import admin
from .models import User, Profile, Image

class ProfileImageInline(admin.TabularInline):
    model = Image
    max_num = 10
    min_num = 1


@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProfileImageInline, ]


admin.site.register(User)
