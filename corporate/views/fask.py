from django.http import request
from django.shortcuts import render
from models.fask import Asks

def Asks(request):
    asks = Asks.objects.all()
    return render(request, 'pages/f-asks.html', context={
        'asks':asks

    } )