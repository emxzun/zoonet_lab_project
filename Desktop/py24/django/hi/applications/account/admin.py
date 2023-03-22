from django.contrib import admin
from applications.account.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)
