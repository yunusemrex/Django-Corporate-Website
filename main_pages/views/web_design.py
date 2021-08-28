from django.shortcuts import render 
from main_pages.models.main_pages import Pages


def web_design(request):
    web_design = Pages.objects.get(title='Web Design')
    return render(request, 'pages/web-desing.html', context={
        'web_design' : web_design
    })