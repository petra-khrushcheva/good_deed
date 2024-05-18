from django.urls import path

from . import views

urlpatterns = [
    path("", views.FundViewSet.as_view()),
]
