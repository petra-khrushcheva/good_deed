from django.db import models

from collects.models import Collect
from core.basemodels import BaseModel


class Payment(BaseModel):
    """Модель единовременного платежа для сбора."""

    collect = models.ForeignKey(
        Collect,
        on_delete=models.PROTECT,
        related_name="payments",
        verbose_name="Сбор",
    )
    amount = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name="Сумма платежа"
    )
    donor_first_name = models.CharField(
        max_length=100, verbose_name="Имя плательщика"
    )
    donor_last_name = models.CharField(
        max_length=100, verbose_name="Фамилия плательщика"
    )
    email = models.EmailField(verbose_name="Email")
    comment = models.TextField(
        verbose_name="Комментарий", blank=True, null=True
    )
    hide_amount = models.BooleanField(
        verbose_name="Скрыть сумму пожертвования", default=False
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return (
            f"{self.donor_first_name} {self.donor_last_name}: "
            f"{self.amount} от {self.created_at}"
        )
