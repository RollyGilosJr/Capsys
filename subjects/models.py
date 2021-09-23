from django.db import models
from django.contrib.auth.models import User
from register.models import UserProfile
from django.db.models import Q

class Subject(models.Model):        
    subject_name = models.CharField(max_length=255, null=True)
    cp_id = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.cp_id
