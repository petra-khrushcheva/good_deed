from django.db import models

from core.basemodels import BaseModel


class Beneficiary(BaseModel):
    """
    Модель благотворительного фонда, в пользу которого может проводиться сбор.
    Экземпляры создаются только сотрудниками сервиса
    после проверки документов фонда.
    """
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Фонд"
        verbose_name_plural = "Фонды"

    def __str__(self):
        return f"{self.name}"
