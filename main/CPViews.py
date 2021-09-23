from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

from proposalgroup.models import Group
from register.models import UserProfile
from subjects.models import Subject

# Create your views here.
@login_required
def home(response):

    #DATABASE QUERIES
    userList = User.objects.all().values('username') #all with username
    userlistnum = User.objects.all().count() #count all users
    student = User.objects.filter(Q(userprofile__role="student")).order_by('date_joined')
    studentnum = UserProfile.objects.filter(role = "4").count() #count all students
    instructornum = UserProfile.objects.filter(role="3").count()  # count all instructor
    subjectnum = Subject.objects.filter(cp_id=response.user.id).count()
    groupnum = Group.objects.all().count()

    name = None
    if response.user.is_authenticated:
        name = response.user.get_full_name()

    return render(response, 'cp/main/home.html', {
        "name":name,
        "userList": userList,
        "userlistnum":userlistnum,
        "student":student,
        "studentnum": studentnum,
        "instructornum": instructornum,
        'groupnum': groupnum,
        'subjectnum':subjectnum



    })

def studentlist(response):
    # student = UserProfile.objects.filter(role = "student") #get all students
    user = User.objects.all()
    student = User.objects.filter(Q(userprofile__role="4")).order_by('date_joined')

    return render(response, 'cp/lists/student.html', {
        "student":student
    })

def grouplist(response):
    group = Group.objects.all()
    return render(response, 'cp/lists/group.html',{
        "group":group
    })

def subjectlist(response):
    # if response.user.userprofile.role == "2":
        cp = UserProfile
        subjects = Subject.objects.filter(cp_id=response.user.id)
        return render(response, 'cp/lists/subject.html', {
            'subjects':subjects
        })

def instructorlist(response):
    instructors = User.objects.filter(Q(userprofile__role="3")).order_by('date_joined')
    return render(response, 'cp/lists/instructor.html', {
        "instructors":instructors
    })
