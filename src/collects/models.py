from django.contrib.auth import get_user_model
from django.db import models

from core.basemodels import BaseModel
from funds.models import Fund

User = get_user_model()


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
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Запланированная сумма",
    )
    image = models.ImageField(
        verbose_name="Изображение", upload_to="collects/"
    )
    completion_datetime = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата и время завершения"
    )
    organizer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="collects",
        verbose_name="Организатор",
    )
    fund = models.ForeignKey(
        Fund,
        on_delete=models.PROTECT,
        related_name="collects",
        verbose_name="Получатель",
    )
    occasion = models.CharField(
        max_length=100,
        choices=CollectOccasion,
        verbose_name="Повод",
        default=CollectOccasion.JUST_LIKE_THAT,
    )
    problem = models.CharField(
        max_length=100, choices=CollectProblem, verbose_name="Проблема"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Сбор"
        verbose_name_plural = "Сборы"

    def __str__(self):
        return f"{self.name} от {self.created_at}"
