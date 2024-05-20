from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from .models import Fund
from .serializers import common, nested


class FundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = common.FundSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            return Fund.objects.prefetch_related(
                "collects__payments", "collects__organizer"
            ).all()
        if self.action == "list":
            return Fund.objects.prefetch_related("collects").all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return common.FundSerializer
        if self.action == "list":
            return nested.FundListSerializer

    @method_decorator(cache_page(60 * 2))
    def dispatch(self, *args, **kwargs):
        return super(FundViewSet, self).dispatch(*args, **kwargs)
