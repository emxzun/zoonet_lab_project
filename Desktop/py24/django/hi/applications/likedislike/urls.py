from django.urls import path

from applications.likedislike.views import LikeCreateAPIView, SetDislikeAPIView



urlpatterns = [
    path('like/', LikeCreateAPIView.as_view()),
    path('dislike/', SetDislikeAPIView.as_view()),

]