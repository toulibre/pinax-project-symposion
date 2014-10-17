# -*- coding: utf-8 -*-
# monkey_patching day __unicode__

from symposion.schedule.models import Day

def day_print(self):
    return "%s - %s" % (self.date, self.schedule.section.name,)

Day.add_to_class("__unicode__", day_print)
