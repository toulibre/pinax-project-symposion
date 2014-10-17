from django.conf.urls.defaults import url, patterns


urlpatterns = patterns("cdl.schedule.views",
    url(r"^$", "schedule_conference", name="schedule_conference"),
    url(r"^([\w\-]+)/list/$", "schedule_list_category", name="schedule_list_category"),
    url(r"^([\w\-]+)/([\w\-]+)/list/$", "schedule_list_category", name="schedule_list_category"),
)
