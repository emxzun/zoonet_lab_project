from django.core.mail import send_mail


def send_chat_mail(email):
    send_mail(
        'This person want to chat to you',
        'kadirbekova43@gmail.com',
        'kadirbekova43@gmail.com',
        [email],
        fail_silently=False,
    )