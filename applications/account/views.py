from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwner

from applications.account.models import Profile
from applications.account.serializers import RegisterSerializer, ForgotPasswordSerializer, ForgotPasswordCompleteSerializer, ChangePasswordSerializer, ProfileSerializer

User = get_user_model()


class RegisterApiView(APIView):

    @staticmethod
    def post(request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались! Подтвердите свою почту или номер телефона!', status=201)


class ActivationApiView(APIView):
    @staticmethod
    def get(request):
        try:
            user = User.objects.get(activation_code=request.data.get('code'))
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'message': 'успешно'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Неверный код'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]


class ForgotPasswordApiView(APIView):
    @staticmethod
    def post(request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля')


class ForgotCompleteAPIView(APIView):

    @staticmethod
    def post(request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Вы успешно сменили пароль!')


class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Вы успешно изменили свой пароль')