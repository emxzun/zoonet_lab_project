# Generated by Django 4.1.7 on 2023-03-22 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('TEXT', 'text'), ('IMAGE', 'image'), ('VIDEO', 'video')], max_length=10)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='chat/images')),
                ('video', models.FileField(null=True, upload_to='video/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('block_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_user', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_chat', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_chat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]