from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models import Collect


class CollectNestedSerializer(serializers.ModelSerializer):
    """Схема для получения денежного сбора."""

    organizer = serializers.StringRelatedField(read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Collect
        fields = [
            "organizer",
            "name",
            "amount",
            "image",
            "completion_datetime",
            "occasion",
        ]
