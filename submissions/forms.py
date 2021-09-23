from .models import Submissions, Submit
from django import forms

class SubmissionsForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ('title','sub_details','image')

class SubmitForm(forms.ModelForm):
    class Meta:
        model = Submit
        fields = ('sub_content', 'image')
