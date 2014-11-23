from django import forms
from django.utils.translation import ugettext_lazy as _

from cdl.coverage.models import Coverage, COVERAGE_TYPES

class CoverageForm(forms.ModelForm):

    coverage_type = forms.CharField(
        widget=forms.RadioSelect(
            choices=COVERAGE_TYPES, attrs={'class':'form-inline'})
        )
    class Meta:
        model = Coverage
        fields = [
            "title",
            "coverage_type",
            "licence",
            "url",
            "url2",
            "poster",
            #~ "coverage_file",
        ]
