from django.urls import path
from rest_framework.routers import  SimpleRouter

from applications.chat.views import MessageViewSet, ChatViewSet

router = SimpleRouter()
router.register('messages', MessageViewSet)
router.register('chat', ChatViewSet)


urlpatterns = router.urls