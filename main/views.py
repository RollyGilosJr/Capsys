from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as DefaultLoginView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from register.models import UserProfile

# Create your views here.
@login_required
def main(response):

    if response.user.userprofile.role == "1":
        return redirect("dean_home")
    elif response.user.userprofile.role == "2":
        return redirect("cp_home")
    elif response.user.userprofile.role == "3":
        return redirect("faculty_home")
    elif response.user.userprofile.role == "4":
        return redirect("cp_home")
    else:
        return redirect("test")

def test(response):
    return render(response,'test.html')