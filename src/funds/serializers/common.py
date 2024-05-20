from rest_framework import serializers

from collects.serializers.nested import CollectNestedSerializer

from ..models import Fund


class FundSerializer(serializers.ModelSerializer):
    """
    Схема для отображения полного описания фонда
    со списком всех сборов в его пользу.
    """

    collects = CollectNestedSerializer(many=True)

    class Meta:
        model = Fund
        fields = ["name", "summary", "description", "collects"]
