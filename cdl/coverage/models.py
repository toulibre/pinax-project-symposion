from django.db import models
from django.utils.translation import ugettext_lazy as _

from symposion.proposals.models import uuid_filename
from symposion.schedule.models import Presentation

COVERAGE_TYPES = (
    ('link', _(u"Link")),
    ('video', _(u"Video")),
    ('audio', _(u"Audio")),
    ('photos', _(u"Photos")),
    ('writeup', _(u"Write-up")),
    ('slides', _(u"Slides")),
    ('transcription', _(u"Transcription")),
)


class Licence(models.Model):
    """
    Coverage licence
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    url = models.URLField(verbose_name=_(u"Url to licence text"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u"Licence")


class Coverage(models.Model):
    """
    Add one or several coverage for a presentation.
    """

    presentation = models.ForeignKey(Presentation, related_name="coverages", blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name=_(u"Link text"))
    coverage_type = models.CharField(max_length=30, choices=COVERAGE_TYPES, verbose_name=_(u"Coverage type"))
    licence = models.ForeignKey(Licence, verbose_name=_(u"Coverage licence"),)
    url = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    poster = models.FileField(upload_to=uuid_filename, blank=True)
    coverage_file = models.FileField(upload_to=uuid_filename, blank=True)

    def __unicode__(self):
        return u"%s - %s" % (self.title, self.presentation)
