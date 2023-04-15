from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.announcement.views import AnnouncementAPIView


router = DefaultRouter()
router.register('', AnnouncementAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
