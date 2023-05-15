# third parties
from django.urls import path

# local
from . import views


urlpatterns = [
    path("", views.index, name="index"),
]
