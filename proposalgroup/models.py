from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



class Group(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    # name1 = models.CharField(max_length=1000,  null=True)
    # name2 = models.CharField(max_length=1000,  null=True)
    # name3 = models.CharField(max_length=1000,  null=True)
    # name4 = models.CharField(max_length=1000,  null=True)
    #
    # def __str__(self):
    #     return self.name1 + " Group"
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    groupname = models.CharField(max_length=225, default="")
    name1 = models.CharField(max_length=1000,  null=True)
    name2 = models.CharField(max_length=1000,  null=True)
    name3 = models.CharField(max_length=1000,  null=True)
    name4 = models.CharField(max_length=1000,  null=True)


    def __str__(self):
        return self.groupname