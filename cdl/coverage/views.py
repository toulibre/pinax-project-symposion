from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from cdl.coverage.forms import CoverageForm
from symposion.schedule.models import Presentation
from cdl.coverage.models import Coverage, COVERAGE_TYPES
from cdl.proposals.models import ProposalCategory


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


def coverage_list(request, coverage_type=None):
    """
    Display all coverage
    """

    coverage_types = []
    for cov_type in COVERAGE_TYPES:
        if Coverage.objects.filter(coverage_type = cov_type[0]):
            coverage_types.append({
                'slug': cov_type[0],
                'name': cov_type[1],
                'count': Coverage.objects.filter(coverage_type = cov_type[0]).count()
            })

    results = None
    if coverage_type:
        coverages = Coverage.objects.filter(coverage_type = coverage_type).order_by('presentation__title')
        categories = ProposalCategory.objects.all()
        results = []
        for category in categories:
            presentations = Presentation.objects.exclude(cancelled=True)
            presentations = presentations.filter(proposal_base__talkproposal__category = category)
            coverages_in_category = coverages.filter(presentation__in = presentations)
            results.append({
                'category' : category,
                'coverages' : coverages_in_category,
            }) 

    ctx = {
        "coverage_type" : coverage_type or None,
        "coverage_types": coverage_types,
        "results": results or None,
        }

    return render(request, "coverage/coverage_list.html", ctx)

