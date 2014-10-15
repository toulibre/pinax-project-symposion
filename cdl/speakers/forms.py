from django import forms

from markitup.widgets import MarkItUpWidget

from symposion.speakers.models import Speaker
#~ from cdl.speakers.models import SpeakerVenue


class SpeakerForm(forms.ModelForm):
    
    class Meta:
        model = Speaker
        fields = [
            "name",
            "biography",
            "photo",
            "annotation",
        ]
        widgets = {
            "biography": MarkItUpWidget(),
        }

#~ class SpeakerVenueForm(forms.ModelForm):
    #~ 
    #~ class Meta:
        #~ model = SpeakerVenue
        #~ fields = [
            #~ "speaker",
        #~ ]
