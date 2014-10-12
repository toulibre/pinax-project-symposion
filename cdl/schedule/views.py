from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader, Context

from django.contrib.auth.decorators import login_required

from symposion.schedule.forms import SlotEditForm
from symposion.schedule.models import Schedule, Day, Slot, Presentation
from cdl.schedule.models import PresentationSession
from symposion.schedule.timetable import TimeTable
from symposion.schedule.views import fetch_schedule

from cdl.proposals.models import ProposalCategory



def schedule_list_category(request, slug=None, category_slug=None):
    schedule = fetch_schedule(slug)

    categories = ProposalCategory.objects.all()
    if category_slug:
        category = categories.get(slug=category_slug)
    else:
        category = None

    presentations = Presentation.objects.filter(section=schedule.section)
    presentations = presentations.exclude(cancelled=True)

    presentation_sessions = PresentationSession.objects.all

    if category_slug:
        results = []
        for presentation in presentations:
            if presentation.proposal.category.slug == category_slug:
                results.append(presentation)
        presentations = results
    
    ctx = {
        "schedule": schedule,
        "presentations": presentations,
        "categories" : categories,
        "presentation_sessions" : presentation_sessions,
        "category" : category or None,
    }

    return render(request, "schedule/schedule_list.html", ctx)

