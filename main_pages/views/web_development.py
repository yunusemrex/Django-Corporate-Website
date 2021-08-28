from django.shortcuts import render 
from main_pages.models.main_pages import Pages


def web_development(request):
    web_development = Pages.objects.get(title='Web Development')
    return render(request, 'pages/web-development.html', context={
        'web_development' : web_development
    })