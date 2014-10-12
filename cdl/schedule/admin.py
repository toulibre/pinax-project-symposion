from django.contrib import admin

from cdl.schedule.models import PresentationSession


admin.site.register(
    PresentationSession,
    list_display=("room", "day", "start", "end", "presentation")
)
