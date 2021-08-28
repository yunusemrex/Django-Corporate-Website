from django.shortcuts import render
from corporate.models import Pricing
from main_pages.models.main_pages import Pages



def pricing(request):
    prices = Pages.objects.get(title='Prices')
    plans = Pricing.objects.order_by('price') 
    return render(request, 'sections/pricing.html', context={
        'plans': plans,
        'prices' : prices
    })