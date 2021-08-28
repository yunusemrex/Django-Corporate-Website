from django.shortcuts import render, redirect
from corporate.models.about import AboutDetail, AboutText
from main_pages.models.main_pages import Pages


def about(request):
    about = Pages.objects.get(title='About')
    return render(request, 'pages/about.html', context={
        'about':about
    })
