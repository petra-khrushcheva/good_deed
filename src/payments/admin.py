from django.contrib import admin

from core.basemodels import BaseAdminModel

from .models import Payment


class PaymentAdmin(BaseAdminModel):
    list_display = ["collect", "amount", "donor_first_name", "donor_last_name"]
    list_select_related = ["collect"]
    search_fields = ("name",)


admin.site.register(Payment, PaymentAdmin)
