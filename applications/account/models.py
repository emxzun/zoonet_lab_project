from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=50, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    def create_activation_code(self):
        import random
        code = str(random.randint(1000, 9999))
        self.activation_code = code


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.user}'


class Image(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')