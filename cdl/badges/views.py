# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.template import loader, Context
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from symposion.speakers.models import Speaker
from symposion.teams.models import Membership

@login_required
def badges_list_csv(request):

    if not request.user.is_staff:
        raise Http404()

    attendees = []
    benevoles = Membership.objects.filter(team__slug="benevoles").order_by("user__first_name")
    for benevole in benevoles:
        attendee = {}
        attendee['organisation'] = u" "
        if hasattr(benevole.user,'speaker_profile'):
            attendee['name'] = benevole.user.speaker_profile.name
            attendee['organisation'] = benevole.user.speaker_profile.organisation
        else:
            attendee['name'] = u" ".join([benevole.user.first_name, benevole.user.last_name])
        attendee['function'] = u"Bénévole"
        if benevole.user.is_staff:
            attendee['function'] = u" / ".join([u"Organisation", attendee['function']])
        attendees.append(attendee)

    speakers = Speaker.objects.filter(~Q(copresentations__isnull=True) | ~Q(presentations__isnull=True)).order_by("name")
    for speaker in speakers:
        attendee = {}
        attendee['name'] = speaker.name
        attendee['organisation'] = u""
        if hasattr(speaker, 'organisation'):
            attendee['organisation'] = speaker.organisation
        attendee['function'] = u"Orateur"
        attendees.append(attendee)
    
    
    response = HttpResponse(mimetype="text/csv")
    response["Content-Disposition"] = 'attachment; filename="badges_list.csv"'

    response.write(loader.get_template("badges/badges_list.csv").render(Context({
        "attendees": attendees,
    })))
    return response
