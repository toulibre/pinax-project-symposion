from django.db import models

from symposion.speakers.models import Speaker

class SpeakerVenue(models.Model):

    speaker = models.OneToOneField(Speaker, related_name="speaker_venue")
    need_hosting = models.BooleanField()
    hosting_annontation = models.TextField(null=True)  # staff only
    city_info = models.CharField(max_length=100, null=True)  # staff only

    def __unicode__(self):
        return u"%s" % (self.speaker)

    class Meta:
        ordering = ["speaker"]
