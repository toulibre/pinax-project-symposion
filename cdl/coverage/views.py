from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from cdl.coverage.forms import CoverageForm
from symposion.schedule.models import Presentation
from cdl.coverage.models import Coverage


@login_required
def coverage_add(request, pk):
    """Form to add coverage for a presentation"""

    presentation = get_object_or_404(Presentation, pk=pk)

    if request.method == "POST":
        form = CoverageForm(request.POST)
        if form.is_valid():
            coverage = form.save(commit=False)
            coverage.presentation = presentation
            coverage.save()
            messages.success(request, _("Coverage."))
            return redirect("schedule_presentation_detail", pk)

    else:
        form = CoverageForm()

    return render(request, "coverage/coverage_edit.html", {
        "form": form,
        "presentation": presentation,
    })

@login_required
def coverage_edit(request, pk):
    """Form to edit coverage"""

    coverage = get_object_or_404(Coverage, pk=pk)
    presentation = coverage.presentation

    if request.method == "POST":
        form = CoverageForm(request.POST, instance=coverage)
        if form.is_valid():
            form.save()
            messages.success(request, _("Coverage form has been updated successfully."))
            return redirect("schedule_presentation_detail", presentation.pk)

    else:
        form = CoverageForm(instance=coverage)

    return render(request, "coverage/coverage_edit.html", {
        "form": form,
        "presentation": presentation,
    })
