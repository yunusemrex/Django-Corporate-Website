from django.shortcuts import render
from corporate.models.call_action import CallAction

def CallAction(request):
    actions= CallAction.objects.all()
    return render(request, 'pages/call-action.html', context={
        'actions': actions
    })