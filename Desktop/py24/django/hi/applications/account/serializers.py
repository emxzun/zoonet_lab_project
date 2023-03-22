from datetime import date
from django.contrib.auth import get_user_model
from rest_framework import serializers
from applications.account.models import Profile, Image
from applications.account.send_mail import send_confirmation_email, send_confirmation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=10, write_only=True, required=True)
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'username']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email(user.email, code)
        return user


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(required=False)
    images = ImageSerializer(many=True, read_only=True)
    age = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['user', 'images', 'gender', 'sexual_orientation', 'description', 'status', 'interests', 'birth_date', 'age']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        birth_date = validated_data['birth_date']
        age = date.today()-birth_date
        profile = Profile.objects.create(user=user, age=int((age).days/365.25), **validated_data)
        files_data = request.FILES
        for image in files_data.getlist('images'):
            Image.objects.create(profile=profile, image=image)
        return profile


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.pop('new_password_confirm')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def validate_old_password(self, p):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(p):
            raise serializers.ValidationError('Неверный пароль')
        return p

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с таким email не сущесвтует')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_confirmation_code(email, user.activation_code)


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не найден')
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Неверный код')
        return code

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()
