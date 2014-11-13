# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse
from django.template import loader, Context
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from symposion.speakers.models import Speaker
from symposion.teams.models import Membership
from symposion.sponsorship.models import Sponsor

@login_required
def badges_list_csv(request):

    if not request.user.is_staff:
        raise Http404()

    attendees = []
    benevoles = Membership.objects.filter(team__slug="benevoles").order_by("user__first_name")
    users = [b.user for b in benevoles]
    for user in users:
        attendee = {}
        if hasattr(user,'speaker_profile'):
            attendee['name'] = user.speaker_profile.name
            attendee['organisation'] = user.speaker_profile.organisation
        else:
            attendee['name'] = u" ".join([user.first_name, user.last_name])
        attendee['role'] = u"Bénévole"
        if user.is_staff:
            attendee['role'] = u" / ".join([u"Organisation", attendee['role']])
        attendees.append(attendee)

    speakers = Speaker.objects.filter(~Q(copresentations__isnull=True) | ~Q(presentations__isnull=True)).order_by("name")
    for speaker in speakers:
        attendee = {}
        attendee['name'] = speaker.name or u"_"
        if hasattr(speaker, 'organisation'):
            attendee['organisation'] = speaker.organisation or u""
        presentation_kinds = [presentation.proposal.kind.slug for presentation in speaker.all_presentations]
        attendee_roles = []
        if "stand-associatif" in presentation_kinds:
            attendee_roles.append(u"Stand")
        if "atelier" in presentation_kinds or "conference" in presentation_kinds:
            attendee_roles.append(u"Orateur")
        attendee['role'] = " / ".join(attendee_roles)
        attendees.append(attendee)

    sponsors = Sponsor.objects.exclude(active=False).order_by("contact_name")
    for sponsor in sponsors:
        attendee = {}
        attendee['name'] = sponsor.contact_name or "_"
        attendee['organisation'] = sponsor.name
        attendee['role'] = u"Sponsor"
        attendees.append(attendee)
        

    response = HttpResponse(mimetype="text/csv")
    response["Content-Disposition"] = 'attachment; filename="badges_list.csv"'

    response.write(loader.get_template("badges/badges_list.csv").render(Context({
        "attendees": attendees,
    })))
    return response
