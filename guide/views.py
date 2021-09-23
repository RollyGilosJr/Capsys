from django.shortcuts import render, redirect
from .forms import GuideForm
from .models import guide


# Create your views here.


def Guide(request):
    if request.user.userprofile.role == "2" or request.user.userprofile.role == "1":
        if request.method == "POST":
            form = GuideForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()
            else:
                form = GuideForm()
        else:
            form = GuideForm()
        posted = guide.objects.all()


        return render(request, 'cp/guide/guide.html', {
            'form': form,
            'posted': posted
        })
    else:
        posted = guide.objects.all()
        return render(request, 'faculty/guide/guide.html', {
            'posted': posted
        })




def guidepost(response, id):
    guideposts = guide.objects.get(id=id)
    return render(response, 'cp/guide/guidepost.html',
              {
                  "guideposts": guideposts
              })
