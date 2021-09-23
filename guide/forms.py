from django import forms
from .models import guide

class GuideForm(forms.ModelForm):

    class Meta:
        model = guide
        fields = ['title','content','pdf','image']