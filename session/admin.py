from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from session.models import Session, Construction


class SessionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', )
    list_display_links = ('id', 'title', )
    actions = ['prepare_session', ]

    def prepare_session(self, request, queryset):
        for obj in queryset:
            obj.prepare_session()
    prepare_session.short_description = "게임 준비"


class ConstructionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'card', 'position', 'order', )
    list_display_links = ('id', )


admin.site.register(Session, SessionAdmin)
admin.site.register(Construction, ConstructionAdmin)