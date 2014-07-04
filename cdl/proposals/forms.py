from django import forms

from markitup.widgets import MarkItUpWidget
from django.utils.translation import ugettext_lazy as _

from .models import TalkProposal, TutorialProposal


class ProposalForm(forms.ModelForm):
    
    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                _(u"The description must be less than 400 characters")
            )
        return value


class TalkProposalForm(ProposalForm):

    class Meta:
        model = TalkProposal
        fields = [
            "title",
            "category",
            "audience_level",
            "description",
            "abstract",
            "duration",
            "additional_notes",
            "recording_release",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }


class TutorialProposalForm(ProposalForm):

    class Meta:
        model = TutorialProposal
        fields = [
            "title",
            "category",
            "audience_level",
            "description",
            "abstract",
            "duration",
            "additional_notes",
            "recording_release",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }
