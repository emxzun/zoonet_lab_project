from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()
class Block(models.Model):
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_by')
    blocked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_user')
    blocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blocked_user', 'blocked_by')


class Chat(models.Model):
    class Type(models.TextChoices):
        TEXT = 'TEXT', _('text')
        IMAGE = 'IMAGE', _('image')
        VIDEO = 'VIDEO', _('video')

    sender = models.ForeignKey(User, related_name='sent_chat', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='receiver_chat', on_delete=models.CASCADE)
    block_user = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='block_user',null=True, default=0)
    type = models.CharField(max_length=10, choices=Type.choices)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="chat/images",blank=False, null=True)
    video = models.FileField(upload_to='video/',null=True,blank=False )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"chat_{self.pk}"


# from django.core.mail import send_mail
# from django.dispatch import receiver
# from django.db.models.signals import post_save
#
# @receiver(post_save, sender=Chat)
# def send_chat_email(sender, instance, created, **kwargs):
#     if created:
#         send_mail(
#             'Chat Notification',
#             'You have a new chat!',
#             'kadirbekova43@gmail.com',
#             [instance.recipient.email],
#             fail_silently=False,
#         )