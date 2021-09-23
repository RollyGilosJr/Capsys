from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
from register.models import UserProfile
from django.db.models import Q
# from .forms import CourseForm

def Add_course(response):
    courses = Course.objects.all()
    if response.user.userprofile.role == "1":
        if response.method == "POST":
            course_name = response.POST.get('course_name')
            course_model = Course(course_name=course_name)
            course_model.save()
        return render(response, 'add_course.html', {'courses':courses})
