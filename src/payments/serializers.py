from rest_framework import serializers

from .models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    """Схема для создания платежа."""

    class Meta:
        model = Payment
        fields = [
            "collect",
            "amount",
            "donor_first_name",
            "donor_last_name",
            "email",
            "comment",
            "hide_amount",
        ]


class PaymentReadSerializer(serializers.ModelSerializer):
    """Схема для отображения платежа в ленте сбора."""

    class Meta:
        model = Payment
        fields = [
            "collect",
            "amount",
            "donor_full_name",
            "comment",
            "hide_amount",
            "created_at",
        ]
