from django.urls import path
from applications.chat.views import ChatCreateAPIView

urlpatterns = [

    path('chat/', ChatCreateAPIView.as_view()),

]
