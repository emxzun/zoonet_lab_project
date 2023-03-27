
# from rest_framework.routers import DefaultRouter
# from .views import ChatViewSet, ChatNotificationAPIView
# from . import consumers


from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
]


# router = DefaultRouter()
# router.register('chats', ChatViewSet, basename='chats')
#
# urlpatterns = [
#     path('notifications/', ChatNotificationAPIView.as_view(), name='chat-notification'),
#     path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi(), name='chat-room'),
# ] + router.urls

