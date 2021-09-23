from django.urls import path
from . import views
from django.conf.urls import url
from django.db.models import Q
from register.models import UserProfile

urlpatterns = [
    path('add_subject/', views.Add_subject, name="Add_Subject"),
    path('manage_subject/', views.Manage_subject, name='Manage_Subject'),
    path('delete_subject/<subject_id>/', views.Delete_subject, name='Delete_Subject'),

]
