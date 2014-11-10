# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader, Context

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from symposion.speakers.models import Speaker
from symposion.teams.models import Team


def badges_list_csv(request):

    if not request.user.is_staff:
        raise Http404()

    attendees = []
    benevoles_team = Team.objects.filter(slug="benevoles")[0]
    #~ import pdb;pdb.set_trace()
    benevoles = benevoles_team.members() # + benevoles_team.managers()
    for benevole in benevoles:
        attendee = {}
        if hasattr(benevole.user,'speaker_profile'):
            attendee['name'] = benevole.user.speaker_profile.name
        else:
            attendee['name'] = u" ".join([benevole.user.first_name, benevole.user.last_name])
        attendee['organisation'] = u" "
        attendee['function'] = u"Bénévole"
        attendees.append(attendee)

    speakers = Speaker.objects.exclude(presentations__isnull=True)
    for speaker in speakers:
        attendee = {}
        attendee['name'] = speaker.name
        attendee['organisation'] = u" "
        attendee['function'] = u"Orateur"
        attendees.append(attendee)
    
    
    response = HttpResponse(mimetype="text/csv")
    response["Content-Disposition"] = 'attachment; filename="badges_list.csv"'

    response.write(loader.get_template("badges/badges_list.csv").render(Context({
        "attendees": attendees,
    })))
    return response
