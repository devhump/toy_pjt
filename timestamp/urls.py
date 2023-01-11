from django.urls import path
from . import views

app_name = "timestamp"

urlpatterns = [
    path("", views.index, name="index"),
]
