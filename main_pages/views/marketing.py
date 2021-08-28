from main_pages.models.main_pages import Pages
from django.shortcuts import render


def marketing(request):
    marketing = Pages.objects.get(title='Marketing')
    return render(request, 'pages/marketing.html', context={
        'marketing': marketing
    })