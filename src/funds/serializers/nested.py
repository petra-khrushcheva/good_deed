from rest_framework import serializers

from ..models import Fund


class FundListSerializer(serializers.ModelSerializer):
    """
    Схема для отображения краткого описания фонда.
    """

    class Meta:
        model = Fund
        fields = ["id", "name", "summary"]
