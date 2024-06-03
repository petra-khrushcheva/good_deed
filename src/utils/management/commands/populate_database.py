from datetime import timezone

import factory
import factory.django
import faker
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from collects.models import Collect
from funds.models import Fund
from payments.models import Payment

User = get_user_model()

FAKE = faker.Faker("ru_RU")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    first_name = factory.LazyFunction(FAKE.first_name)
    last_name = factory.LazyFunction(FAKE.last_name)
    email = factory.LazyFunction(FAKE.email)
    username = factory.LazyFunction(FAKE.user_name)


class FundFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Fund

    name = factory.LazyFunction(FAKE.company)
    summary = factory.LazyAttribute(lambda _: FAKE.sentence(nb_words=8))
    description = factory.LazyAttribute(
        lambda _: FAKE.paragraph(nb_sentences=5)
    )


class CollectFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Collect

    name = factory.LazyAttribute(lambda _: FAKE.sentence(nb_words=8))
    description = factory.LazyAttribute(
        lambda _: FAKE.paragraph(nb_sentences=5)
    )
    amount = factory.LazyAttribute(
        lambda _: FAKE.pyint(min_value=1000, max_value=1000000)
    )
    image = "media/test_image_for_factory_boy.jpeg"
    completion_datetime = factory.LazyAttribute(
        lambda _: FAKE.date_time_this_year(
            tzinfo=timezone.utc, before_now=False, after_now=True
        )
    )
    organizer = factory.Iterator(User.objects.all())
    fund = factory.Iterator(Fund.objects.all())
    occasion = factory.LazyAttribute(
        lambda _: FAKE.enum(enum_cls=Collect.CollectOccasion)
    )
    problem = factory.LazyAttribute(
        lambda _: FAKE.enum(enum_cls=Collect.CollectProblem)
    )


class PaymentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Payment

    collect = factory.Iterator(Collect.objects.all())
    amount = factory.LazyAttribute(
        lambda _: FAKE.pyint(min_value=10, max_value=10000)
    )
    donor_first_name = factory.LazyFunction(FAKE.first_name)
    donor_last_name = factory.LazyFunction(FAKE.last_name)
    email = factory.LazyFunction(FAKE.email)
    comment = factory.LazyAttribute(lambda _: FAKE.sentence(nb_words=5))
    hide_amount = factory.LazyAttribute(
        lambda _: FAKE.pybool(truth_probability=20)
    )


class Command(BaseCommand):
    help = "Populate the database."

    def handle(self, *args, **options):
        for _ in range(1000):
            UserFactory()

        for _ in range(1000):
            FundFactory()

        for _ in range(1000):
            CollectFactory()

        for _ in range(1000):
            PaymentFactory()
