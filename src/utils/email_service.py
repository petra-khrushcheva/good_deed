from functools import wraps

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage

CREATE_COLLECT_SUBJECT = "Вы создали сбор!"
CREATE_COLLECT_BODY_TEMPLATE = (
    "{}! Вы создали сбор {} в пользу фонда {}. Спасибо вам за вашу помощь!"
)
MAKE_PAYMENT_SUBJECT = "Спасибо за вашу помощь!"
MAKE_PAYMENT_BODY_TEMPLATE = (
    "{} {}! Вы совершили платеж на сумму {} в пользу фонда {}. "
    "Фонд и {} благодарны вам за вашу помощь."
)


def create_mail(subject, body_template):
    def decorator(func):
        @wraps(func)
        def wrapper(email_to, *args, **kwargs):
            email = EmailMessage(
                subject=subject,
                body=body_template.format(*args, **kwargs),
                from_email=settings.EMAIL_HOST_USER,
                to=[email_to],
            )
            result = email.send()
            return result

        return wrapper

    return decorator


@shared_task
@create_mail(
    subject=CREATE_COLLECT_SUBJECT, body_template=CREATE_COLLECT_BODY_TEMPLATE
)
def send_create_collect_mail(email_to, full_name, collect_name, fund_name):
    return


@shared_task
@create_mail(
    subject=MAKE_PAYMENT_SUBJECT, body_template=MAKE_PAYMENT_BODY_TEMPLATE
)
def send_make_payment_mail(
    email_to, first_name, last_name, amount, fund_name, organizer_name
):
    return
