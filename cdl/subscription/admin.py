from django.contrib import admin

from cdl.subscription.models import Attendee, Subscription


admin.site.register(
    Attendee,
    list_display=("name", "email")
)

admin.site.register(Subscription)
