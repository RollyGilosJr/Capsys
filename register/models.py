from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)

    roles = (
        ('1','Dean'),
        ('2', 'Capstone Professor'),
        ('3', 'Faculty'),
        ('4', 'Student'),
    )
    role = models.CharField(max_length=100, choices=roles, default="instructor")
    image = models.ImageField(upload_to="images/",default="user.png")
    group_name = models.CharField(default="", max_length=250)


    def __str__(self):
        return self.user.username

