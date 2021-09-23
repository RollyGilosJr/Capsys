from django.shortcuts import render

# Create your views here.
def PanelistsView(response):
    return render(response,'cp/proposals/panelists/panelists.html')