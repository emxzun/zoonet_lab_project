from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.favorite.views import FavoriteAPIView


router = DefaultRouter()
router.register('', FavoriteAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
