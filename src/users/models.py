from django.contrib.auth.models import AbstractUser

from core.basemodels import BaseModel


class User(BaseModel, AbstractUser):
    pass
