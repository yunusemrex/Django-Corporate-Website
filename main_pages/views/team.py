from django.shortcuts import render, redirect
from corporate.models.team import TeamMembers
from main_pages.models.main_pages import Pages



def team(request):
    members = TeamMembers.objects.all()
    team = Pages.objects.get(title='Team')
    return render(request, 'pages/team.html', context={
        'members': members,
        'team' : team
    })