from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import request
from rest_framework.response import Response
from applications.announcement.models import Announcement
from applications.favorite.models import Favorite
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from applications.favorite.serializers import FavoriteSerializer

User = get_user_model()

class FavoriteAPIView(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    def create(self, announcement_id):
        announcement = Announcement.objects.get(id=announcement_id)
        current_user = request.user
        if current_user.is_authenticated:
            favorites_count = announcement.favorites_count(current_user)
        else:
            favorites_count = announcement.favorites_count(None)

        return Response({'favorites_count': favorites_count})

