from rest_framework import serializers

from ..models import Collect
from payments.serializers import PaymentReadSerializer
from funds.serializers.nested import FundListSerializer


class CollectCreateSerializer(serializers.ModelSerializer):
    """Схема для создания денежного сбора."""

    occasion = serializers.ChoiceField(choices=Collect.CollectOccasion)
    problem = serializers.ChoiceField(choices=Collect.CollectProblem)

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

    class Meta:
        model = Collect
        fields = [
            "name",
            "amount",
            "description",
            "image",
            "completion_datetime",
        ]
