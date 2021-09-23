from django.urls import path
from . import views

urlpatterns = [
    path("proposal/panelists/", views.PanelistsView, name="Panelist"),


]
