from django.urls import path
from .views import RoomList, RoomDetail

urlpatterns = [
    path('rooms/', RoomList.as_view()),
    path('rooms/<slug:slug>/', RoomDetail.as_view()),
]
