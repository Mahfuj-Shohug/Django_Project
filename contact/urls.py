from django.urls import path
from . import views

urlpatterns = [
    path("massage/", views.contactFrom),
]
