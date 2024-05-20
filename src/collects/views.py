from django.db.models import Count, Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.response import Response

from utils.email_service import send_create_collect_mail
from utils.permission import OrganizerOrReadOnly

from .models import Collect
from .serializers import common


class CollectViewSet(viewsets.ModelViewSet):
    queryset = (
        Collect.objects.select_related("organizer", "fund")
        .annotate(
            participants_count=Count("payments"),
            amount_collected=Sum("payments__amount"),
        )
        .prefetch_related("payments")
        .all()
    )

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return common.CollectUpdateSerializer
        if self.action == "create":
            return common.CollectCreateSerializer
        return common.CollectReadSerializer

    permission_classes = (OrganizerOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("problem", "occasion", "fund")

    @method_decorator(cache_page(60 * 2))
    def dispatch(self, *args, **kwargs):
        return super(CollectViewSet, self).dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = common.CollectCreateSerializer(data=request.data)
        if serializer.is_valid():
            collect_data = serializer.validated_data
            collect_data.organizer = user
            collect = Collect.objects.create(**collect_data)
            send_create_collect_mail.delay(
                email_to=user.email,
                full_name=user.get_full_name(),
                collect_name=collect.name,
                fund_name=collect.fund.name,
            )
            return Response(collect, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        collect = Collect.objects.get(pk)
        collect.is_active = False
        collect.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
