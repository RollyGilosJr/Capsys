from django.urls import path,include
from . import views


urlpatterns = [
    path('forum/', views.forum, name="forum"),
    path('forum/<int:id>', views.discussion, name="discussion"),
    path('discussion/<int:id>/', views.comments, name='discussion_info'),


    path('forum/edit/<int:id>', views.update_topic, name="update_topic"),
    path('forum/<int:id>/edit/', views.update_forum, name="update_forum"),
    path('discussion/edit/<int:id>/', views.update_reply, name='update_reply'),

]
