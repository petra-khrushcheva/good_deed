import functools
from django.conf import settings
from django.core.mail import send_mail


# написать декоратор


def mail_template(subject: str, message: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(recipient_list):
            return func(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list,
            )
        return wrapper
    return decorator


@mail_template(subject="Создание сбора", message="Вы создали сбор")
def collect_create_mail(recipient_list):
    send_mail(recipient_list=recipient_list)
