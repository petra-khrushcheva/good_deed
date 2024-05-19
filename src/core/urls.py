from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from collects.views import CollectViewSet
from funds.views import FundViewSet
from payments.views import PaymentCreateViewSet

router = DefaultRouter()

router.register(r"collects", CollectViewSet)
router.register(r"funds", FundViewSet)
router.register(r"payments", PaymentCreateViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
