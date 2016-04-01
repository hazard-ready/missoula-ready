from django.contrib.gis import admin
from embed_video.admin import AdminVideoMixin
from solo.admin import SingletonModelAdmin
######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminModelImports
from .models import EmbedSnugget, TextSnugget, SnuggetSection, SnuggetSubSection, Location, SiteSettings, SupplyKit, ImportantLink, Fire_Burn_Probability2, Flood_Worst_Case, EQ_Fault_Buffer, Fire_Worst_Case_ph2, EQ_Fault_Worst, EQ_Historic_Distance, EQ_Fault_Shaking, Flood_FEMA_DFRIM_2015, Fire_Hist_Bound, winterstorm, summerstorm, Landslide_placeholder2, Flood_Channel_Migration_Zones
# END OF GENERATED CODE BLOCK
######################################################
from .models import PastEventsPhoto, DataOverviewImage
admin.site.register(SnuggetSection, admin.ModelAdmin)
admin.site.register(SnuggetSubSection, admin.ModelAdmin)


class SnuggetAdmin(admin.ModelAdmin):
######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminLists
    list_display = ('shortname', 'section', 'sub_section', 'Fire_Burn_Probability2_filter', 'Flood_Worst_Case_filter', 'EQ_Fault_Buffer_filter', 'Fire_Worst_Case_ph2_filter', 'EQ_Fault_Worst_filter', 'EQ_Historic_Distance_filter', 'EQ_Fault_Shaking_filter', 'Flood_FEMA_DFRIM_2015_filter', 'Fire_Hist_Bound_filter', 'winterstorm_filter', 'summerstorm_filter', 'Landslide_placeholder2_filter', 'Flood_Channel_Migration_Zones_filter')
    list_filter = ('section', 'sub_section', 'Fire_Burn_Probability2_filter', 'Flood_Worst_Case_filter', 'EQ_Fault_Buffer_filter', 'Fire_Worst_Case_ph2_filter', 'EQ_Fault_Worst_filter', 'EQ_Historic_Distance_filter', 'EQ_Fault_Shaking_filter', 'Flood_FEMA_DFRIM_2015_filter', 'Fire_Hist_Bound_filter', 'winterstorm_filter', 'summerstorm_filter', 'Landslide_placeholder2_filter', 'Flood_Channel_Migration_Zones_filter')

    fieldsets = (
        (None, {
            'fields': ('section', 'sub_section')
        }),
        ('Filters', {
            'description': 'Choose a filter value this snugget will show up for.  It is recommended you only select a value for one filter and leave the rest empty.',
            'fields': (('Fire_Burn_Probability2_filter', 'Flood_Worst_Case_filter', 'EQ_Fault_Buffer_filter', 'Fire_Worst_Case_ph2_filter', 'EQ_Fault_Worst_filter', 'EQ_Historic_Distance_filter', 'EQ_Fault_Shaking_filter', 'Flood_FEMA_DFRIM_2015_filter', 'Fire_Hist_Bound_filter', 'winterstorm_filter', 'summerstorm_filter', 'Landslide_placeholder2_filter', 'Flood_Channel_Migration_Zones_filter'))
        })
    )
# END OF GENERATED CODE BLOCK
######################################################

    def shortname(self, obj):
        return "Undefined"


class TextAdmin(SnuggetAdmin):
    fieldsets = SnuggetAdmin.fieldsets + ((None, {
        'fields': ('content',),
        }),
    )

    def shortname(self, obj):
        return 'Text: "' + str(obj) + '"'


class EmbedAdmin(AdminVideoMixin, SnuggetAdmin):
    fieldsets = SnuggetAdmin.fieldsets + ((None, {
        'fields': ('embed',),
        }),
    )

    def shortname(self, obj):
        return "EmbedSnugget"

admin.site.register(TextSnugget, TextAdmin)
admin.site.register(EmbedSnugget, EmbedAdmin)


class GeoNoEditAdmin(admin.GeoModelAdmin):
    modifiable = False

admin.site.register(ImportantLink, admin.ModelAdmin)
admin.site.register(SiteSettings, SingletonModelAdmin)
admin.site.register(Location, SingletonModelAdmin)
admin.site.register(SupplyKit, SingletonModelAdmin)
admin.site.register(PastEventsPhoto, admin.ModelAdmin)
admin.site.register(DataOverviewImage, admin.ModelAdmin)

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminSiteRegistrations
admin.site.register(Fire_Burn_Probability2, GeoNoEditAdmin)
admin.site.register(Flood_Worst_Case, GeoNoEditAdmin)
admin.site.register(EQ_Fault_Buffer, GeoNoEditAdmin)
admin.site.register(Fire_Worst_Case_ph2, GeoNoEditAdmin)
admin.site.register(EQ_Fault_Worst, GeoNoEditAdmin)
admin.site.register(EQ_Historic_Distance, GeoNoEditAdmin)
admin.site.register(EQ_Fault_Shaking, GeoNoEditAdmin)
admin.site.register(Flood_FEMA_DFRIM_2015, GeoNoEditAdmin)
admin.site.register(Fire_Hist_Bound, GeoNoEditAdmin)
admin.site.register(winterstorm, GeoNoEditAdmin)
admin.site.register(summerstorm, GeoNoEditAdmin)
admin.site.register(Landslide_placeholder2, GeoNoEditAdmin)
admin.site.register(Flood_Channel_Migration_Zones, GeoNoEditAdmin)
# END OF GENERATED CODE BLOCK
######################################################

