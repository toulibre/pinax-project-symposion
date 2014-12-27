from django.conf.urls.defaults import *


urlpatterns = patterns("cdl.coverage.views",
    url(r"^presentation/(?:(?P<pk>\d+)/)?add/$", "coverage_add", name="coverage_add"),
    url(r"^(?:(?P<pk>\d+)/)?edit/$", "coverage_edit", name="coverage_edit"),
    url(r"^$", "coverage_list", name="coverage_list"),
    url(r"^([\w\-]+)$", "coverage_list", name="coverage_list"),
)
