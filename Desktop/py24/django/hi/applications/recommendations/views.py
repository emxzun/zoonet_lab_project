from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from applications.account.models import Profile
from applications.recommendations.serializers import RecommendationsSerializer
from applications.recommendations.filterbackend import FilterProfileBackend


class RecommendationsApiView(ListAPIView):
    '''Список рекомендованных пользователей с одинаковыми Интересами, Статусом, Ориентации'''
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = RecommendationsSerializer
    filter_backends = [FilterProfileBackend]

    

