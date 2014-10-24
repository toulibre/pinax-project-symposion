from django import forms

from markitup.widgets import MarkItUpWidget

from cdl.subscription.models import Attendee


class AttendeeForm(forms.ModelForm):
    
    class Meta:
        model = Attendee
        fields = [
            "email",
            "name",
            "interests",
        ]
        widgets = {
            "interests": MarkItUpWidget(),
        }
