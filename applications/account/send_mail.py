from django.core.mail import send_mail


def send_confirmation_email(email, code):
    send_mail(
        'Подтверждение',
        f'http://localhost:8000/api/v1/account/activate/{code}',
        'e352709@gmail.com',
        [email]
    )


def send_confirmation_code(email, code):
    send_mail(
        'Подтверждение',
        code,
        'e352709@gmail.com',
        [email]
    )