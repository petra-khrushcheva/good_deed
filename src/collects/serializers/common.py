from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from funds.serializers.nested import FundListSerializer
from payments.serializers import PaymentReadSerializer

from ..models import Collect


class CollectCreateSerializer(serializers.ModelSerializer):
    """Схема для создания денежного сбора."""

    occasion = serializers.ChoiceField(choices=Collect.CollectOccasion)
    problem = serializers.ChoiceField(choices=Collect.CollectProblem)
    image = Base64ImageField()

    class Meta:
        model = Collect
        fields = [
            "name",
            "description",
            "amount",
            "image",
            "completion_datetime",
            "fund",
            "occasion",
            "problem",
        ]


class CollectReadSerializer(serializers.ModelSerializer):
    """Схема для получения денежного сбора."""

    payments = PaymentReadSerializer(many=True)
    fund = FundListSerializer()
    organizer = serializers.StringRelatedField(read_only=True)
    image = Base64ImageField()
    amount_collected = serializers.IntegerField()
    participants_count = serializers.IntegerField()

    class Meta:
        model = Collect
        fields = [
            "organizer",
            "name",
            "description",
            "amount",
            "amount_collected",
            "image",
            "completion_datetime",
            "fund",
            "occasion",
            "participants_count",
            "payments",
        ]


class CollectUpdateSerializer(serializers.ModelSerializer):
    """
    Схема для редактирования описания одного денежного сбора.
    Фонд, в пользу которого проводится сбор, и повод изменять нельзя.
    """

    image = Base64ImageField()

    class Meta:
        model = Collect
        fields = [
            "name",
            "amount",
            "description",
            "image",
            "completion_datetime",
        ]
