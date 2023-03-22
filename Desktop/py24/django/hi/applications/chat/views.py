from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from applications.chat.serializers import ChatSerializer
from rest_framework.views import APIView

class ChatCreateAPIView(APIView):
    serializer_class = ChatSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        message = 'chat notification successfully!'
        response = {
            'data': data,
            'message': message
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
