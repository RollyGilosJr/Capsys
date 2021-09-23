from django.shortcuts import render,redirect


def home(response):
    return render(response, 'faculty/main/home.html')

