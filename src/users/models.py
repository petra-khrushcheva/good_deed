from django.contrib.auth.models import AbstractUser

from core.basemodels import BaseModel


class User(BaseModel, AbstractUser):
    def __str__(self) -> str:
        return self.get_full_name()
