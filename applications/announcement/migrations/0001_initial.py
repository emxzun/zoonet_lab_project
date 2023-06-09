# Generated by Django 4.2 on 2023-04-14 20:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Дата обновления')),
                ('description', models.TextField(verbose_name='Описание')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('price', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Цена должна быть: договорная или 0 до 1000000', regex='^(договорная|\\d{1,7})$')], verbose_name='Цена')),
                ('is_promotion', models.BooleanField(default=False, verbose_name='Оплата рекламы')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно/Неактивно')),
                ('category', models.CharField(choices=[('сельско-хозяйственные', 'сельско-хозяйственные'), ('собаки', 'собаки'), ('кошки', 'кошки'), ('птицы', 'птицы'), ('рыбки', 'рыбки'), ('грызуны', 'грызуны'), ('рептилии', 'рептилии'), ('амфибии', 'амфибии'), ('насекомые', 'насекомые'), ('паукообразные', 'паукообразные'), ('хостелы/приюты', 'хостелы/приюты'), ('вет.клиники', 'вет.клиники'), ('ветеринары', 'ветеринары'), ('зоо няни', 'зоо няни'), ('зоо магазины', 'зоо магазины')], max_length=25)),
                ('location', models.CharField(choices=[('Кыргызстан', 'Кыргызстан'), ('Бищкек', 'Бищкек'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Иссык-Куль', 'Иссык-Куль'), ('Баткен', 'Баткен'), ('Талас', 'Талас'), ('Джалал-Абад', 'Джалал-Абад')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='ImageAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='announcement/image')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='announcement.announcement')),
            ],
            options={
                'verbose_name': 'Фотография объявления',
                'verbose_name_plural': 'Фотографии объявления',
            },
        ),
    ]
