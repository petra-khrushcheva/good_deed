from django.contrib import admin

from core.basemodels import BaseAdminModel
from .models import Beneficiary


class BeneficiaryAdmin(BaseAdminModel):
    list_display = ["name", "description"]
    search_fields = ("name",)


admin.site.register(Beneficiary, BeneficiaryAdmin)
