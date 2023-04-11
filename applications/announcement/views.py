from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from applications.announcement.models import Announcement


User = get_user_model()


class AnnouncementAPIView(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = Announcement
    permission_classes = [IsAuthenticated]
