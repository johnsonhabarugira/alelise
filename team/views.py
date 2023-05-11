from django.shortcuts import render
from .models import TeamMember
import requests

def our_team(request):
    ip_address = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/'.format(ip_address)
    response = requests.get(url)
    data = response.json()
    country = data.get('country')
    team_members = TeamMember.objects.all()
    return render(request, 'team/our_team.html', {'team_members': team_members,'country':country})
