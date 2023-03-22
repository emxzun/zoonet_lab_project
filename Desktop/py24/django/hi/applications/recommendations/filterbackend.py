from rest_framework.filters import BaseFilterBackend
from applications.account.models import Profile

class FilterProfileBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id = request.user.id
        user_interests = Profile.objects.get(user_id=user_id).interests
        user_status = Profile.objects.get(user_id=user_id).status
        user_sexual_orientation = Profile.objects.get(user_id=user_id).sexual_orientation
        queryset = queryset.filter(interests=user_interests, 
                                   status=user_status, 
                                   sexual_orientation=user_sexual_orientation).exclude(user_id=user_id)
        return queryset