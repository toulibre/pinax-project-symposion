from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from cdl.subscription.forms import AttendeeForm, SubscriptionForm
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
            messages.success(request, _("You subscribed successfully."))
            return redirect("schedule_presentation_detail", presentation.pk)

    else:
        form = AttendeeForm()

    return render(request, "subscription/subscribe_to.html", {
        "form": form,
        "presentation": presentation,
    })

@login_required
def subscription_add(request, pk):
    """Form to add subscription form to a presentation"""

    presentation = get_object_or_404(Presentation, pk=pk)

    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.presentation = presentation
            subscription.save()
            messages.success(request, _("Subscription form has been created successfully."))
            return redirect("dashboard")

    else:
        form = SubscriptionForm()

    return render(request, "subscription/subscription_edit.html", {
        "form": form,
        "presentation": presentation,
    })

@login_required
def subscription_edit(request, pk):
    """Form to edit subscription form for a presentation"""

    presentation = get_object_or_404(Presentation, pk=pk)
    subscription = presentation.subscription

    if request.method == "POST":
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, _("Subscription form has been updated successfully."))
            return redirect("dashboard")

    else:
        form = SubscriptionForm(instance=subscription)

    return render(request, "subscription/subscription_edit.html", {
        "form": form,
        "presentation": presentation,
    })
