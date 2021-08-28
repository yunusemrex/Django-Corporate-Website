from django.shortcuts import render, redirect
from corporate.models.about import AboutDetail, AboutText


def about(request):
    atext = AboutText.objects.all()
    return render(request, 'pages/about.html', context={
        'atext': atext
    })
