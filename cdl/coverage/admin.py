from django.contrib import admin

from .models import Licence, Coverage


admin.site.register(Coverage)
admin.site.register(Licence,
    prepopulated_fields={"slug": ("name",)},
)
