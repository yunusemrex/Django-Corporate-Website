from django.shortcuts import render
from main_pages.models.main_pages import Pages


def graphic_design(request):
    graphic_design = Pages.objects.get(title='Graphic Design')
    return render(request, 'pages/graphic-design.html', context={
        'graphic_design': graphic_design
    })