from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>/", views.monthNumber),
    path("<str:month>/", views.monthlyChallanges),
]
