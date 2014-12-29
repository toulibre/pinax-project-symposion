import os
import urlparse

from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

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

MEDIA_EXTENSION = ['mp4', 'webm', 'ogv', 'ogg', 'mp3', 'flac']


def generate_filename(instance, filename):
    folder_name = slugify(instance.presentation.title)
    return os.path.join("coverage", folder_name, filename)


def get_extension(url):
    """get extension from url"""
    path = urlparse.urlparse(url).path
    return os.path.splitext(path)[1][1:]


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
    url2 = models.URLField(blank=True, help_text=_(u"Url to another format for audio or video media."))
    poster = models.URLField(blank=True)
    coverage_file = models.FileField(upload_to=generate_filename, verbose_name=_(u"Coverage file"), blank=True)

    def __unicode__(self):
        return u"%s - %s" % (self.title, self.presentation)

    def url_extension(self):
        """return url extension if exists
        """
        if hasattr(self, 'url'):
            extension = get_extension(self.url)
            if extension != '' and extension in MEDIA_EXTENSION:
                return extension

    def url2_extension(self):
        """return url extension if exists
        """
        if hasattr(self, 'url'):
            extension = get_extension(self.url2)
            if extension != '' and extension in MEDIA_EXTENSION:
                return extension

    def download_url(self):
        if self.coverage_file:
            return reverse("file_download", args=[self.pk, os.path.basename(self.file.name).lower()])

    def get_url(self):
        if self.url:
            return self.url
        elif self.url2:
            return self.url2
        elif self.coverage_file:
            return self.coverage_file.url
        else:
            return None
