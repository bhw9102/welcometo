from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from session.models import Session, Construction


class SessionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', )
    list_display_links = ('id', 'title', )


class ConstructionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'card', 'position', 'order', )
    list_display_links = ('id', )


admin.site.register(Session, SessionAdmin)
admin.site.register(Construction, ConstructionAdmin)