from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from applications.feedback.models import Feedback
from applications.feedback.serializers import FeedbackSerializer

User = get_user_model()

class FeedbackAPIView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

