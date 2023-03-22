from django.urls import path

from applications.likedislike.views import LikeCreateAPIView, SetDislikeAPIView, GetLikeDislikeAPIView



urlpatterns = [
    path('like/', LikeCreateAPIView.as_view()),
    path('dislike/<int:recipient_id>/', SetDislikeAPIView.as_view()),
    path('get_status_like/<int:recipient_id>/', GetLikeDislikeAPIView.as_view()),
]