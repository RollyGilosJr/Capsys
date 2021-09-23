from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from .models import Group
from django.contrib.auth.models import User
from register.models import UserProfile
from django.contrib import messages


def Groupview(response):

    if response.user.userprofile.role == "4":

        users = User.objects.exclude(id=response.user.id).exclude(is_superuser=True)
        name = response.user
        group = Group.objects.filter(user=name)



        if response.method == "POST":
            user = response.user
            groupname = response.POST.get('name1') + ' Group'
            name1 = response.POST.get('name1')
            name2 = response.POST.get('name2')
            name3 = response.POST.get('name3')
            name4 = response.POST.get('name4')
            select = Group(user = user, name1=name1, name2=name2, name3=name3, name4=name4, groupname=groupname)
            select.save()

            messages.success(response,'Group successfully created')

            grp = Group.objects.get(user=response.user)
            grpname = grp.groupname

            mem1 = User.objects.get(username=grp.name1.lower())
            mem1use = mem1.userprofile
            mem1use.group_name = grpname
            mem1use.save()
            mem2 = User.objects.get(username=grp.name2.lower())
            mem2use = mem2.userprofile
            mem2use.group_name = grpname
            mem2use.save()
            mem3 = User.objects.get(username=grp.name3.lower())
            mem3use = mem3.userprofile
            mem3use.group_name = grpname
            mem3use.save()
            mem4 = User.objects.get(username=grp.name4.lower())
            mem4use = mem4.userprofile
            mem4use.group_name = grpname
            mem4use.save()

        return render(response, 'student/proposals/group/group.html', {
            'users': users,
            'name': name,
            'group':group,

        })
    elif response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        group = Group.objects.all()
        return render(response, 'cp/proposals/group/group.html',{
            'group':group
        })
