from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import UserProfile


def register(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        profile_form = UserProfileForm(response.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect("/")
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()
    return render(response, 'registration/register.html', {
        "form": form,
        "profile_form":profile_form
    })

@login_required
def profile(response):

    if response.method == 'POST':
        p_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.userprofile)
        u_form = UserUpdateForm(response.POST, instance=response.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(response, 'Your Profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.userprofile)

    context = {'p_form': p_form, 'u_form': u_form}
    return render(response, 'registration/profile.html', context)

