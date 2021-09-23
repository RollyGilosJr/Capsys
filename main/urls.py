from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views, CPViews, DeanViews, FacultyViews, StudentViews
from register import views as regviews
from django.contrib.auth import views as auth_views #import this

from register import views as regviews



urlpatterns =[

#URLS of all USERS#
    path('', views.main, name= "home"),
    path('list/student/', CPViews.studentlist, name="studentlist"),
    path('list/group/', CPViews.grouplist, name="grouplist"),
    path('list/instructor/', CPViews.instructorlist, name="instructorlist"),
    path('list/subject/', CPViews.subjectlist, name='subjectlist'),
    url('login/', LoginView.as_view(redirect_authenticated_user=True)),


#CAPSTONE PROFESSOR URLS#
    path('cp_home/',CPViews.home, name="cp_home"),

#DEPARTMENT DEAN URLS#
    path('dean_home/', DeanViews.home, name="dean_home"),
    path('add_cp/', DeanViews.add_cp, name="add_cp"),
    path('add_faculty/', DeanViews.add_faculty, name="add_faculty"),
    path('add_student/', DeanViews.add_student, name="add_student"),
    path('add_group/', DeanViews.add_group, name="add_group"),

    #FACULTY URLS#
    path('faculty_home/',FacultyViews.home, name="faculty_home"),

#STUDENT URLS#
    path('student_home/', StudentViews.Home, name='student_home'),
    path('student_course/', StudentViews.Course, name="student_course"),


#TEST URLS#
    path('testlogin',views.test,name='test')
]
