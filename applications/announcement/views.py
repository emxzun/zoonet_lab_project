from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from applications.announcement.models import Announcement
from applications.announcement.serializers import AnnouncementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

User = get_user_model()

class AnnouncementAPIView(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'price', 'location']
    search_fields = ['description']
