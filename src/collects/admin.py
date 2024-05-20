from django.contrib import admin

from core.basemodels import BaseAdminModel

from .models import Collect


class CollectAdmin(BaseAdminModel):
    list_display = [
        "name",
        "description",
        "amount",
        "fund",
        "organizer",
    ]
    list_select_related = [
        "fund",
        "organizer",
    ]
    search_fields = ("name",)


admin.site.register(Collect, CollectAdmin)
