from django.urls import path

from . import views

urlpatterns = [
    path("", views.trips_page, name="trips"),
]
