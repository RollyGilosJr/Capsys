from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Submissions, Submit
from .forms import SubmissionsForm, SubmitForm

@login_required
def submissions(response):
    if response.user.userprofile.role == "2" or response.user.userprofile.role == "1" :

        form = SubmissionsForm()
        if response.method == 'POST':
            form = SubmissionsForm(response.POST)
            if form.is_valid():
                user = response.user
                title = response.POST.get('title')
                duedate = response.POST.get('duedate')
                sub_details = response.POST.get('sub_details')
                image = response.POST.get('image')
                filetype = response.POST.get('filetype')
                submission = Submissions(user=user, title=title, duedate=duedate, sub_details=sub_details, image=image, filetype=filetype)
                submission.save()
                return redirect('/submissions/')
        submissions = Submissions.objects.filter().order_by('-timestamp')

        return render (response, 'cp/submissions/submissions.html', {'submissions':submissions, 'form':form})

    elif response.user.userprofile.role == "3" or response.user.userprofile.role == "4" :
        submissions = Submissions.objects.filter().order_by('-timestamp')

        return render(response, 'student/submissions/submissions.html',{
            'submissions':submissions,
        })

def submit(response, id):

    if response.user.userprofile.role == "3" or response.user.userprofile.role == "4" :

        postsub = Submissions.objects.filter(id=id).first()
        submits = Submit.objects.filter(postsub=postsub)
        form = SubmitForm()
        if response.method == 'POST':
            form = SubmitForm(response.POST)
            if form.is_valid():
                user = response.user
                submi = response.POST.get('sub_content')
                image = response.POST.get('image')
                submit = Submit(user=user, postsub=postsub, sub_content=submi, image=image )
                submit.save()
                print('here')

        return render (response, 'student/submissions/submit.html', {'postsub': postsub, 'submits':submits, 'form':form})

    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2" :

        postsub = Submissions.objects.filter(id=id).first()
        submits = Submit.objects.filter(postsub=postsub)


        return render (response, 'cp/submissions/submit.html', {'postsub': postsub, 'submits':submits })

