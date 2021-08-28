from django.shortcuts import render
from corporate.models import Pricing


def PlanPricing(request):
    plans = Pricing.objects.order_by('price') 
    return render(request, 'pages/pricing.html', context={
        'plans': plans
    })