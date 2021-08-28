from django.shortcuts import render
from main_pages.models.main_pages import Pages


def policy(request):
    policy = Pages.objects.get(title='Policy')
    return render(request, 'pages/privacy-policy.html', context={
        'policy' : policy
    })