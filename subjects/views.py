from django.shortcuts import render, redirect
from .models import Subject
from django.contrib.auth.models import User
from register.models import UserProfile
from django.contrib import messages
from django.db.models import Q

def Add_subject(response):
    if response.user.userprofile.role == "1":
        CPs = UserProfile.objects.filter(role='2')
        subjects = Subject.objects.all()
        if response.method == "POST":
            subject_name = response.POST.get('subject')
            cp_id = response.POST.get('cps')
            cp = UserProfile.objects.get(id=cp_id)
            code = response.POST.get('code')
            subject = Subject(subject_name=subject_name, cp_id=cp, code=code)
            subject.save()
        return render(response, 'add_subject.html', {'CPs':CPs, 'subjects':subjects})



def Manage_subject(response):
    subjects = Subject.objects.all()
    return render(response, 'manage_subject.html', {'subjects':subjects})


def Edit_subject(response, subject_id):
    subject = Subject.objects.get(id=subject_id)
    CP = UserProfile.objects.filter(role='2')
    if response.method == 'POST':
        subject_id = response.POST.get('subject_id')
        subject_name = response.POST.get('subject')
        cp_id = response.POST.get('cp')

        subject = Subject.objects.get(id=subject_id)
        subject.subject_name = subject_name
        cp = UserProfile.objects.get(id=cp_id)
        subject.cp_id = cp
        subject.save()

        return render(request, 'manage_subject.html', {'subject':subject, 'CP':CP, 'subject_id':subject_id})


# def edit_subject_save(request):
#     if request.method == "POST":
#         HttpResponse("Invalid Method.")
#     else:
#         subject_id = request.POST.get('subject_id')
#         subject_name = request.POST.get('subject')
#         course_id = request.POST.get('course')
#         staff_id = request.POST.get('staff')
#
#         try:
#             subject = Subjects.objects.get(id=subject_id)
#             subject.subject_name = subject_name
#
#             course = Courses.objects.get(id=course_id)
#             subject.course_id = course
#
#             staff = CustomUser.objects.get(id=staff_id)
#             subject.staff_id = staff
#
#             subject.save()
#
#             messages.success(request, "Subject Updated Successfully.")
#             # return redirect('/edit_subject/'+subject_id)
#             return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))
#
#         except:
#             messages.error(request, "Failed to Update Subject.")
#             return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))
#             # return redirect('/edit_subject/'+subject_id)


def Delete_subject(response, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return redirect('Manage_Subject')
