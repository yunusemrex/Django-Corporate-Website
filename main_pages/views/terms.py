from django.shortcuts import render 
from main_pages.models.main_pages import Pages


def terms(request):
    terms = Pages.objects.get(title='Terms')
    return render(request, 'pages/terms.html', context={
        'terms' : terms,
    })