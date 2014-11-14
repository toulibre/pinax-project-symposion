from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from symposion.teams.models import Team, Membership


@login_required
def teams_list_detail(request):
    teams = Team.objects.all()

    return render(request, "teams/teams_list_detail.html", {
        "teams": teams,
    })

