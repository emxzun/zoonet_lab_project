from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.announcement.views import PostAnnouncementAPIView




urlpatterns = [
    path('post/', PostAnnouncementAPIView.as_view(), name='post_announcement'),
   
]
