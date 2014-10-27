from django.conf.urls.defaults import *


urlpatterns = patterns("cdl.subscription.views",
    url(r"^presentation/(?:(?P<pk>\d+)/)?$", "subscribe_to_presentation", name="subscribe_to_presentation"),
    url(r"^presentation/(?:(?P<pk>\d+)/)?add/$", "subscription_add", name="subscription_add"),
    url(r"^presentation/(?:(?P<pk>\d+)/)?edit/$", "subscription_edit", name="subscription_edit"),
)
