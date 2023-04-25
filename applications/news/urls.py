from django.urls import include, path
from rest_framework.routers import DefaultRouter
from applications.news.views import NewsAPIView

router = DefaultRouter()
router.register('', NewsAPIView)

urlpatterns = [
    path('', include(router.urls))
]