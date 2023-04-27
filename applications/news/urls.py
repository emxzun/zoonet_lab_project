from django.urls import include, path
from rest_framework.routers import DefaultRouter
from applications.news.views import NewsAPIView

router = DefaultRouter()
router.register('', NewsAPIView)

urlpatterns = [
    path('', include(router.urls))
<<<<<<< HEAD
]
=======
]
>>>>>>> 489992a1922f2266d32ed71161681565cfd08ae0
