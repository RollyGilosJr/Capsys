from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            print("here")
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            print("here")
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('role', 'image')

    def __init__(self, *args, **kwargs):
        roles = [

            (3, 'Faculty'),
            (4, 'Student'),
        ]
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = roles





class UserUpdateForm(forms.ModelForm):

    # email = forms.EmailField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            print("here")
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            print("here")
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'image']
