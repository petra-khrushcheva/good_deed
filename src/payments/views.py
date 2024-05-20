from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from utils.email_service import send_make_payment_mail

from .models import Payment
from .serializers import PaymentCreateSerializer


class PaymentCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Payment.objects.select_related(
        "collect__fund__name", "collect__organizer"
    ).all()
    serializer_class = PaymentCreateSerializer

    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):

        serializer = PaymentCreateSerializer(data=request.data)
        if serializer.is_valid():
            payment_data = serializer.validated_data
            payment = Payment.objects.create(**payment_data)
            send_make_payment_mail.delay(
                email_to=payment.email,
                first_name=payment.donor_first_name,
                last_name=payment.donor_last_name,
                amount=payment.amount,
                fund_name=payment.collect.fund.name,
                organizer_name=payment.collect.organizer.get_full_name(),
            )
            return Response(payment_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
