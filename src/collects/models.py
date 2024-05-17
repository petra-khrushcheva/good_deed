from django.db import models

from beneficiaries.models import Beneficiary
from core.basemodels import BaseModel
from users.models import User


class Collect(BaseModel):
    """Модель группового денежного сбора."""

    class CollectOccasion(models.TextChoices):
        WEDDING = "Свадьба"
        BIRTHDAY = "День рождения"
        KINDNESS = "Добро без повода"
        WOMEN = "Женское дело"
        PROMOTION = "Повышение"
        JUST_LIKE_THAT = "Просто так"
        BABY_SHOWER = "Рождение ребенка"
        GOOD_HABIT = "Хорошая привычка"

    class CollectProblem(models.TextChoices):
        ADDICTION = "Алкоголизм и наркомания"
        POVERTY = "Бедность"
        HOMELESSNESS = "Бездомность"
        GENDER_INEQUALITY = "Гендерное неравенство"
        DISABILITY = "Инвалидность"
        HUMAN_RIGHTS = "Права человека"
        MENTAL_HEALTH = "Психическое здоровье"
        CULTURE_AND_ART = "Искусство и культура"
        ORPHANHOOD = "Сиротство"
        HOMELESS_ANIMALS = "Бездомные животные"

    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    amount = models.IntegerField(
        null=True, verbose_name="Запланированная сумма"
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="/collects"
    )
    completion_datetime = models.DateTimeField(
        null=True, verbose_name="Дата и время завершения"
    )
    organizer_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="collects",
        verbose_name="Организатор",
    )
    beneficiary = models.ForeignKey(
        Beneficiary,
        on_delete=models.PROTECT,
        related_name="collects",
        verbose_name="Получатель",
    )
    occasion = models.CharField(
        choices=CollectOccasion,
        verbose_name="Повод",
        default=CollectOccasion.JUST_LIKE_THAT,
    )
    problem = models.CharField(choices=CollectProblem, verbose_name="Проблема")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Сбор"
        verbose_name_plural = "Сборы"

    def __str__(self):
        return f"{self.name} от {self.created_at}"
