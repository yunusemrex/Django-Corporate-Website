from django.shortcuts import render, redirect
from corporate.models.services import Services


def Services(request):
    return render(request, 'pages/index.html', context={})