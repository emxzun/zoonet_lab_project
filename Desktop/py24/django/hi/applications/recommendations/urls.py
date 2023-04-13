from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.recommendations.views import RecommendationsApiView


urlpatterns = [
    path('', RecommendationsApiView.as_view(), name='recommendations'),

]
