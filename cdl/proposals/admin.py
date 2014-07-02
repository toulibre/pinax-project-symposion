from django.contrib import admin

from .models import ProposalCategory, TalkProposal, TutorialProposal


admin.site.register(ProposalCategory)
admin.site.register(TalkProposal)
admin.site.register(TutorialProposal)
