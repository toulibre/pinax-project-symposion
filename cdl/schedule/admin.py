from django.contrib import admin

from cdl.schedule.models import PresentationSession


admin.site.register(PresentationSession)

#~ admin.site.register(
    #~ Slot,
    #~ list_display=("day", "start", "end", "kind")
#~ )
#~ admin.site.register(
    #~ SlotRoom,
    #~ list_display=("slot", "room")
#~ )
#~ admin.site.register(Presentation)
