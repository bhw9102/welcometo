from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from game.models import NumberClass, EffectClass, ConstructionClass


class NumberClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'value', )
    list_display_links = ('id', 'value', )


class EffectClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title', )


class ConstructionClassAdmin(ImportExportModelAdmin):
    list_display = ('id', 'number', 'effect', 'count', )
    list_display_links = ('id', )


admin.site.register(NumberClass, NumberClassAdmin)
admin.site.register(EffectClass, EffectClassAdmin)
admin.site.register(ConstructionClass, ConstructionClassAdmin)