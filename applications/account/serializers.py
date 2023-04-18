import vonage
from django.contrib.auth import get_user_model
from rest_framework import serializers
from applications.account.models import Profile, Image
from applications.account.send_mail import send_confirmation_email, send_confirmation_code


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)
    phone_number = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password', 'password2', 'username']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        email = attrs.get('email')
        phone_number = attrs.get('phone_number')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают!')
        elif not email and not phone_number:
            raise serializers.ValidationError('Введите почту или номер телефона!')
        elif phone_number:
            if len(phone_number) < 12 or len(phone_number) > 12:
                raise serializers.ValidationError('Введите корректные данные!')
        return attrs

    @staticmethod
    def validate_username(username):
        if not username:
            raise serializers.ValidationError('Введите username!')
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Пользователь с таким username уже существует!')
        elif len(username) < 6:
            raise serializers.ValidationError('username должен состоять минимум из 6 символов!')
        elif len(username) > 10:
            raise serializers.ValidationError('username может состоять максимум из 10 символов!')
        return username

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        if not user.phone_number:
            send_confirmation_email(user.email, code)
        elif user.phone_number:
            client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
            sms = vonage.Sms(client)
            phone_code = user.phone_number_code
            responseData = sms.send_message(
                {
                    "from": "Vonage APIs",
                    "to": user.phone_number,
                    "text": phone_code,
                }
            )
            if responseData["messages"][0]["status"] == "0":
                print("Message sent successfully.")
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        return user


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    user = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        profile = Profile.objects.create(user=user, **validated_data)
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
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)

    def validate(self, attrs):
        email = attrs.get('email')
        phone_number = attrs.get('phone_number')
        if not email and not phone_number:
            raise serializers.ValidationError('Введите почту или номер телефона!')
        elif not phone_number:
            if not User.objects.filter(email=email).exists():
                raise serializers.ValidationError('Пользователя с таким email не сущесвтует')
        elif phone_number:
            if not User.objects.filter(phone_number=phone_number).exists():
                raise serializers.ValidationError('Пользователя с таким номером не существует')
            elif len(phone_number) < 12 or len(phone_number) > 12:
                raise serializers.ValidationError('Введите корректные данные!')
        return attrs

    def send_code(self):
        phone_number = self.validated_data.get('phone_number')
        email = self.validated_data.get('email')
        if not phone_number:
            user = User.objects.get(email=email)
            user.create_activation_code()
            user.save()
            send_confirmation_code(email, user.activation_code)
        elif not email:
            client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
            sms = vonage.Sms(client)
            user = User.objects.get(phone_number=phone_number)
            user.create_phone_number_code()
            code = user.phone_number_code
            user.save()
            responseData = sms.send_message(
                {
                    "from": "Vonage APIs",
                    "to": phone_number,
                    "text": code,
                }
            )
            if responseData["messages"][0]["status"] == "0":
                print("Message sent successfully.")
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password_confirm')
        code = attrs.get('code')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        elif not User.objects.filter(activation_code=code).exists() \
                and not User.objects.filter(phone_number_code=code).exists():
            raise serializers.ValidationError('Неверный код!')
        return attrs

    def set_new_password(self):
        password = self.validated_data.get('password')
        code = self.validated_data.get('code')
        if User.objects.filter(activation_code=code).exists():
            user = User.objects.get(activation_code=code)
            user.set_password(password)
            user.activation_code = ''
            user.save()
        elif not User.objects.filter(activation_code=code).exists():
            user = User.objects.get(phone_number_code=code)
            user.set_password(password)
            user.phone_number_code = ''
            user.save()