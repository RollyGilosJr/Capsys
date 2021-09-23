from django.urls import path
from . import views

urlpatterns = [
    path("proposal/group/", views.Groupview, name="Group"),

]
