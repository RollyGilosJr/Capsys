from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User

def AdviserView(response):
    return render(response, 'cp/proposals/adviser/adviser.html')