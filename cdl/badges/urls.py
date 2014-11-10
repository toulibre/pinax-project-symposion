from django.conf.urls.defaults import url, patterns


urlpatterns = patterns("cdl.badges.views",
    url(r"^badges_list.csv$", "badges_list_csv", name="badges_list_csv"),
)
