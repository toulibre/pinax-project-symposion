from django.db import models

from symposion.schedule.models import Presentation, Room, Day

# Create your models here.

class PresentationSession(models.Model):

    presentation = models.OneToOneField(Presentation, related_name="presentation")
    room = models.ForeignKey(Room, related_name="room")
    day = models.ForeignKey(Day, related_name="day")
    start = models.TimeField()
    end = models.TimeField()

