from django.urls import path
from . import views

urlpatterns = [
    path("proposal/title/", views.Titleview, name="Title"),
    path("proposal/title/<int:id>", views.TitleCommentview, name="TitleComment"),

]
