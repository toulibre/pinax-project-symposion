from django.conf.urls.defaults import url, patterns


urlpatterns = patterns("cdl.teams.views",
    #~ url(r"^$", "teams_list", name="team_list"),
    url(r"^detail$", "teams_list_detail", name="teams_list_detail"),
)
