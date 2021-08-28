from django.shortcuts import render
from main_pages.models.main_pages import Pages

def get_started(request):
    get_started = Pages.objects.get(title='Get Started')
    return render(request, 'pages/get_started.html', context={
        'get_started': get_started
    })