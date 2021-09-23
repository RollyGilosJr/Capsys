from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('add_course/', views.Add_course, name='Add_Course'),
]
