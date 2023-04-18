from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.feedback.views import FeedbackAPIView
router = DefaultRouter()
router.register('', FeedbackAPIView)

urlpatterns = [
    path('', include(router.urls)),
]