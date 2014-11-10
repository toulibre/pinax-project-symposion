from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

import symposion.views

# from pinax.apps.account.openid_consumer import PinaxConsumer

WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"

urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r"^account/signup/$", symposion.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),
    
    #~ url(r"^partenariat/", direct_to_template, {"template": "sponsorship/list.html"}, name="sponsor_list"),
    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
    url(r"^intervenant/", include("symposion.speakers.urls")),
    url(r"^speaker/", include("cdl.speakers.urls")),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^partenariat/", include("symposion.sponsorship.urls")),
    url(r"^boxes/", include("symposion.boxes.urls")),
    url(r"^teams/", include("symposion.teams.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^subscribe/", include("cdl.subscription.urls")),
    url(r"^schedule/", include("cdl.schedule.urls")),
    url(r"^programme/", include("cdl.schedule.urls")),

    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r"^programme/", include("symposion.schedule.urls")),
    url(r"^conference/", include("symposion.conference.urls")),
    url(r"^badges/", include("cdl.badges.urls")),
    url(r"^markitup/", include("markitup.urls")),
    
    url(r"^", include("symposion.cms.urls")),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
