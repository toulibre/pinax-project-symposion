
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from cdl.subscription.forms import AttendeeForm
from cdl.subscription.models import Attendee
from symposion.schedule.models import Presentation

def subscribe_to_presentation(request, pk):
    """Form to subscribe"""

    presentation = get_object_or_404(Presentation, pk=pk)

    if request.method == "POST":
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.subscribe_to = presentation.subscription
            attendee.save()
            messages.success(request, "You subscribed successfully.")
            return redirect("schedule_presentation_detail", presentation.pk)

    else:
        form = AttendeeForm()

    return render(request, "subscription/subscribe_to.html", {
        "form": form,
        "presentation": presentation,
    })
