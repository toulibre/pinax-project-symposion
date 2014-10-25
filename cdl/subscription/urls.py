from django.conf.urls.defaults import *


urlpatterns = patterns("cdl.subscription.views",
    url(r"^presentation/(?:(?P<pk>\d+)/)?$", "subscribe_to_presentation", name="subscribe_to_presentation"),
)
