from django.contrib import admin

from cdl.schedule.models import PresentationSession


admin.site.register(
    PresentationSession,
    list_display=("day", "room", "start", "end", "presentation")
)
