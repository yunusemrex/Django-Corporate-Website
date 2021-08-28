from django.shortcuts import render, redirect
from corporate.models.services import Services
from main_pages.models.main_pages import Pages



def services(request):
    services = Pages.objects.get(title='Services')
    return render(request, 'pages/services.html', context={
        'services': services
    })