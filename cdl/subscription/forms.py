from django import forms
from django.utils.translation import ugettext_lazy as _

from markitup.widgets import MarkItUpWidget

from cdl.subscription.models import Attendee
from cdl.subscription.utils import validate_3_plus_4

class AttendeeForm(forms.ModelForm):

    captcha = forms.IntegerField(help_text=_(u"How much 3 + 4 makes?"), validators=[validate_3_plus_4])

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
