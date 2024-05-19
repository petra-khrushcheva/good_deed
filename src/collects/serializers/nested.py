from rest_framework import serializers

from ..models import Collect


class CollectNestedSerializer(serializers.ModelSerializer):
    """Схема для получения денежного сбора."""

    organizer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Collect
        fields = [
            "organizer",
            "name",
            "amount",
            "amount_collected",
            "image",
            "completion_datetime",
            "occasion",
        ]
