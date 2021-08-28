from django.http import request
from django.shortcuts import redirect, render
from corporate.models import why_us_asks
from corporate.models.fask import Asks
from corporate.models import Pricing, TeamMembers, ContactModel
from corporate.forms import ContactForm
from django.core.paginator import Paginator
from django.core import paginator
from corporate.models.services import Services
from corporate.models.call_action import CallAction
from corporate.models.hero import HeroSection
from corporate.models.why_us import WhyUs
from corporate.models.why_us_asks import WhyUsAsks
from corporate.models.about import AboutText, AboutDetail

# Create your views here.

def index(request):
    asks = Asks.objects.all()
    plans = Pricing.objects.order_by('price')
    members = TeamMembers.objects.all()
    services = Services.objects.all()
    actions = CallAction.objects.all()
    adetail_heading = AboutDetail.objects.all()
    atext = AboutText.objects.all()
    headers = HeroSection.objects.all()
    why_us = WhyUs.objects.all()
    why_asks = WhyUsAsks.objects.all()

    # member = request.GET.get('member')

    # paginator = Paginator(members, 4)

    return render(request, 'pages/index.html', context={
        'asks': asks,
        'plans': plans,
        'members': members,
        'services': services,
        'actions': actions,
        'adetail' : adetail_heading,
        'atext' : atext,
        'headers': headers,
        'why_us' : why_us,
        'why_asks' : why_asks,
    })


# def inner(request):
#     return render(request, 'pages/inner-page.html', context={

#     })


def detail(request):
    return render(request, 'pages/portfolio-details.html', context={

    })
