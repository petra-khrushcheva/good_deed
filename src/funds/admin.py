from django.contrib import admin

from core.basemodels import BaseAdminModel
from .models import Fund


class FundAdmin(BaseAdminModel):
    list_display = ["name", "description"]
    search_fields = ("name",)


admin.site.register(Fund, FundAdmin)
