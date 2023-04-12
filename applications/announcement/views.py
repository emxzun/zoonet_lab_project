from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from applications.announcement.models import Announcement
from applications.announcement.serializers import AnnouncementSerializer


User = get_user_model()


class PostAnnouncementAPIView(APIView):
    '''Создание объявления происходит
       с помощью form-data, необходимо заполнить следующие поля:
        "description": "Описание объявления",
        "images": "прикрепленные файлы: images",
        "phone": "номер телефона",
        "price": "цена: значения должны быть: "договорная" или 0 до 1000000",
        "category": "сельско-хозяйственные, собаки, кошки, птицы, рыбки, грызуны, рептилии, амфибии, насекомые, паукообразные, хостелы/приюты, вет.клиники, ветеринары, зоо няни, зоо магазины",
        "location": "Кыргызстан, Бищкек, Ош, Нарын, Иссык-Куль, Баткен, Талас, Джалал-Абад"'''
    
    serializer_class = AnnouncementSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        data = serializer.data
        message = 'Объявление создано.'
        response = {
            'data': data,
            'message': message
        }
        return Response(response, status=status.HTTP_201_CREATED)


        


    
