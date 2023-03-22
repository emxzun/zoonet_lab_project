from django.db import models
from applications.account.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class LikeDislike(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                                          related_name='like_sent',
                                          verbose_name="user_id - Кто поставил лайк/дизлайк")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE,
                                           related_name='like_received',
                                           verbose_name="user_id - На кого поставили лайк/дизлайк")
    is_like = models.BooleanField(default=False)
    is_dislike = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"is_like-{self.is_like}, is_dislike-{self.is_dislike}"

    class Meta:
        verbose_name = 'Лайк-Дизлайк'
