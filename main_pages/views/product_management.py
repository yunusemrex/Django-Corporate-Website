from django.shortcuts import render 
from main_pages.models.main_pages import Pages


def product_management(request):
    product_management = Pages.objects.get(title='Product Management')
    return render(request, 'pages/product-management.html', context={
        'product_management' : product_management,
    })