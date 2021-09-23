from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import ProposeTitleForm, TitleCommentForm
from .models import ProposeTitle, TitleComment

def Titleview(response):

    if response.user.userprofile.role == "4":

        form = ProposeTitleForm()

        if response.method == "POST":
            form = ProposeTitleForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                save.save()

                return redirect('Title')
        titlelist = ProposeTitle.objects.all()

        return render(response, 'student/proposals/title/title.html',{
            "titlelist": titlelist,
            "form":form
        })
    else:
        titlelist = ProposeTitle.objects.all()
        return render(response,'cp/proposals/title/title.html',{
            'titlelist':titlelist
        })

def TitleCommentview(response, id):
    title = ProposeTitle.objects.filter(id=id).first()
    title_comment = TitleComment.objects.filter(title = title)
    form = TitleCommentForm()

    if response.method == "POST":
        form = TitleCommentForm(response.POST)
        if form.is_valid():
            save = form.save(commit=False)
            save.author = response.user
            save.title = title
            save.save()
    return render(response, 'student/proposals/title/titlecomment.html',{
        'title':title,
        'comment': title_comment,
        'form':form
    })

