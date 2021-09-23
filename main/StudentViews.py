from django.shortcuts import render,redirect
from subjects.models import Subject

def Home(response):
    return render(response, 'student/main/home.html')

def Course(response):
    subjects = Subject.objects.all()
    return render(response, 'student/main/student_courses.html', {'subjects':subjects})
