from django.db.models import Q
from django.shortcuts import render,redirect
from register.forms import RegisterForm, UserProfileForm
from register.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from proposalgroup.models import Group



def home(response):
    cpnum = UserProfile.objects.filter(role="2").count()  # count all students
    instructornum = UserProfile.objects.filter(role="3").count()  # count all instructor
    studentnum = UserProfile.objects.filter(role="4").count()  # count all students
    groupnum = Group.objects.all().count()

    name = None

    if response.user.is_authenticated:
        name = response.user.get_full_name()

    return render(response, 'dean/main/home.html',{
        "name":name,
        "cpnum":cpnum,
        "instructornum":instructornum,
        "studentnum":studentnum,
        "groupnum":groupnum,
    })

def add_cp(response):
    cp = User.objects.filter(Q(userprofile__role="2")).order_by('date_joined')

    if response.method == "POST":
        first_name = response.POST.get("first_name")
        last_name = response.POST.get("last_name")
        username = response.POST.get("username")
        email = response.POST.get("email")
        password = "!@#Default"
        role = "2"

        try:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            profile = UserProfile.objects.create(user=user,role=role)
            user.save()
            profile.save()
            return redirect('add_cp')
        except:
            messages.error(response, "Failed to ADD Staff!")
            return redirect('add_cp')

    return render(response, 'dean/main/add/add_cp.html',{
        "cp":cp
    })

def add_faculty(response):
    faculty = User.objects.filter(Q(userprofile__role="3")).order_by('date_joined')

    if response.method == "POST":
        first_name = response.POST.get("first_name")
        last_name = response.POST.get("last_name")
        username = response.POST.get("username")
        email = response.POST.get("email")
        password = "!@#Default"
        role = "3"

        try:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            profile = UserProfile.objects.create(user=user,role=role)
            user.save()
            profile.save()
            return redirect('add_faculty')
        except:
            messages.error(response, "Failed to ADD Staff!")
            return redirect('add_faculty')

    return render(response, 'dean/main/add/add_faculty.html',{
        "faculty":faculty
    })


def add_student(response):
    student = User.objects.filter(Q(userprofile__role="4")).order_by('date_joined')

    if response.method == "POST":
        first_name = response.POST.get("first_name")
        last_name = response.POST.get("last_name")
        username = response.POST.get("username")
        email = response.POST.get("email")
        password = "!@#Default"
        role = "4"

        try:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            profile = UserProfile.objects.create(user=user,role=role)
            user.save()
            profile.save()
            return redirect('add_student')
        except:
            messages.error(response, "Failed to ADD Staff!")
            return redirect('add_student')

    return render(response, 'dean/main/add/add_student.html',{
        "student":student
    })

def add_group(response):
    group = Group.objects.all()
    return render(response,'dean/main/add/add_group.html',{
        'group':group
    })