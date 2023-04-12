from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Announcement(models.Model):
    '''Модель Объявление'''
    created_at = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='Дата создания')
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
    is_active = models.BooleanField(blank=False, null=False, default=True, verbose_name='Активно/Неактивно')

    CategoryChoices = (
        ('сельско-хозяйственные', 'сельско-хозяйственные'),
        ('собаки', 'собаки'),
        ('кошки', 'кошки'),
        ('птицы', 'птицы'),
        ('рыбки', 'рыбки'),
        ('грызуны', 'грызуны'),
        ('рептилии', 'рептилии'),
        ('амфибии', 'амфибии'),
        ('насекомые', 'насекомые'),
        ('паукообразные', 'паукообразные'),
        ('хостелы/приюты', 'хостелы/приюты'),
        ('вет.клиники', 'вет.клиники'),
        ('ветеринары', 'ветеринары'),
        ('зоо няни', 'зоо няни'),
        ('зоо магазины', 'зоо магазины'),
    )
    category = models.CharField(choices=CategoryChoices, max_length=25)

    LocationChoices = (
        ('Кыргызстан', 'Кыргызстан'),
        ('Бищкек', 'Бищкек'),
        ('Ош', 'Ош'),
        ('Нарын', 'Нарын'),
        ('Иссык-Куль', 'Иссык-Куль'),
        ('Баткен', 'Баткен'),
        ('Талас', 'Талас'),
        ('Джалал-Абад', 'Джалал-Абад')
    )
    location = models.CharField(choices=LocationChoices, max_length=15)


    def __str__(self) -> str:
        return f"СТАТУС: {self.is_active}, РЕКЛАМА: {self.is_promotion}, КАТЕГОРИЯ: {self.category}, ЛОКАЦИЯ: {self.location}, ОПИСАНИЕ: {self.description}"
    
    class Meta:
        verbose_name = 'Оъявление'
        verbose_name_plural = 'Оъявления'



