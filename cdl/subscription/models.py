from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from symposion.schedule.models import Presentation

class Subscription(models.Model):
    """A subscription object linked to a presentation
    """

    presentation = models.OneToOneField(Presentation, related_name="subscription")
    max_attendees = models.IntegerField()

    def __unicode__(self):
        return _(u"Subscription to %s") % self.presentation
    
    def all_attendees(self):
        return self.attendees.all()

    @property
    def attendees_nb(self):
        return self.attendees.count()

    def is_closed(self):
        """True if max attendees number is reached"""
        return self.max_attendees <= self.attendees_nb

class Attendee(models.Model):
    """Attendee to a talk or a presentation
    """

    #~ user = models.OneToOneField(User, null=True, related_name="attendee_profile")
    subscribe_to = models.ForeignKey('Subscription', related_name="attendees")
    email = models.EmailField(help_text=_(u"Used in case of cancelling"))
    name = models.CharField(max_length=100, help_text="Your name")
    interests = models.TextField(help_text=_(u"Your project"), null=True, blank=True)

    def __unicode__(self):
        return self.name
