from django.db import models

from symposion.schedule.models import Presentation, Room, Day

# Create your models here.

class PresentationSession(models.Model):

    presentation = models.OneToOneField(Presentation, related_name="session")
    day = models.ForeignKey(Day, related_name="day")
    start = models.TimeField()
    end = models.TimeField()
    room = models.ForeignKey(Room, related_name="room", null=True, blank=True)

    def __unicode__(self):
        return u"%s - %s to %s : %s" % (self.day, self.start, self.end, self.presentation, )

    class Meta:
        ordering = ["day", "room", "start", "end"]
