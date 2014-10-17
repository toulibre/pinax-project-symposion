import itertools
import operator

from django.db.models import Count, Min

from symposion.schedule.models import Room
from symposion.schedule.timetable import pairwise
from cdl.schedule.models import PresentationSession


class TimeTable(object):
    
    def __init__(self, day):
        self.day = day
    
    def sessions_qs(self):
        qs = PresentationSession.objects.all()
        qs = qs.filter(day=self.day)
        return qs
    
    def rooms(self):
        qs = Room.objects.all()
        #~ qs = qs.filter(schedule=self.day.schedule)
        #~ qs = qs.filter(pk__in=PresentationSession.objects.filter(room__in=self.sessions_qs().values("pk")).values("room"))
        qs = qs.order_by("order")
        return qs
    
    def __iter__(self):
        times = sorted(set(itertools.chain(*self.sessions_qs().values_list("start", "end"))))
        slots = PresentationSession.objects.filter(pk__in=self.sessions_qs().values("pk"))
        slots = slots.annotate(room_count=Count("room"), order=Min("room__order"))
        slots = slots.order_by("start", "order")
        row = []
        for time, next_time in pairwise(times):
            row = {"time": time, "slots": []}
            for slot in slots:
                if slot.start == time:
                    slot.rowspan = TimeTable.rowspan(times, slot.start, slot.end)
                    slot.colspan = slot.room_count
                    row["slots"].append(slot)
            if row["slots"] or next_time is None:
                yield row
    
    @staticmethod
    def rowspan(times, start, end):
        return times.index(end) - times.index(start)
#~ 
#~ class TimeList(object):
    #~ """Return session list by room"""
#~ 
    #~ def __init__(self, day):
        #~ self.day = day
#~ 
    #~ def rooms(self):
        #~ qs = Room.objects.all()
        #~ qs = qs.filter(schedule=self.day.schedule)
        #~ qs = qs.filter(pk__in=PresentationSession.objects.filter(room__in=self.sessions_qs().values("pk")).values("room"))
        #~ qs = qs.order_by("order")
        #~ return qs
#~ 
    #~ def __iter__():
        #~ times = sorted(set(itertools.chain(*self.sessions_qs().values_list("start", "end"))))
        #~ slots = PresentationSession.objects.filter(pk__in=self.sessions_qs().values("pk"))
        #~ slots = slots.order_by("start", "order")
        #~ for room in rooms:
            #~ session_room = slots.filter(room=room)
            #~ 
        #~ 
