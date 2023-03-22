from django.core.mail import send_mail


def send_like_mail(email):
    send_mail(
        'This person liked you',
        'kadirbekova43@gmail.com',
        'kadirbekova43@gmail.com',
        [email],
        fail_silently=False,
    )