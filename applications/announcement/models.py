from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Announcement(models.Model):
    '''Модель Объявление'''
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    images = models.ImageField(upload_to='announcement/images', blank=True, null=True, verbose_name='Изображения')
    description = models.TextField(blank=False, null=False, verbose_name='Описание')
    phone = models.CharField(blank=False, null=False, verbose_name='Номер телефона', max_length=15)
    price = models.CharField(blank=False, null=False, verbose_name='Цена', max_length=10,
                             validators=[RegexValidator(regex=r'^(договорная|\d{1,7})$',
                                                        message='Цена должна быть: договорная или 0 до 1000000')
                                                        ])
    is_promotion = models.BooleanField(blank=False, null=False, default=False, verbose_name='Оплата рекламы')

    CategoryChoices = (
        ('SA', 'сельско-хозяйственные животные'),
        ('DO', 'собаки'),
        ('CA', 'кошки'),
        ('BE', 'птицы'),
        ('FI', 'рыбки'),
        ('RO', 'грызуны'),
        ('RE', 'рептилии'),
        ('AM', 'амфибии'),
        ('IN', 'насекомые'),
        ('AR', 'паукообразные'),
        ('HS', 'хостелы/приюты'),
        ('VC', 'вет.клиники'),
        ('VE', 'ветеринары'),
        ('ZN', 'зоо няни'),
        ('ZM', 'зоо магазины'),
    )
    category = models.CharField(choices=CategoryChoices, max_length=2)

    LocationChoices = (
        ('KYR', 'Кыргызстан'),
        ('BIS', 'Бищкек'),
        ('OSH', 'Ош'),
        ('NAR', 'Нарын'),
        ('ISS', 'Иссык-Куль'),
        ('BAT', 'Баткен'),
        ('TAL', 'Талас'),
        ('JAL', 'Джалал-Абад')
    )
    location = models.CharField(choices=LocationChoices, max_length=3)

 

    class Meta:
        verbose_name = 'Оъявление'
        verbose_name_plural = 'Оъявления'



