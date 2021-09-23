from django.urls import path
from . import views

urlpatterns = [
    path("proposal/adviser/", views.AdviserView, name="Adviser"),


]
