from django.db import models
from applications.announcement.models import Announcement
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f'{self.user.username}---{self.announcement}'

    def favorites_count(self, current_user):
        return self.favorites.exclude(user=current_user).count()
