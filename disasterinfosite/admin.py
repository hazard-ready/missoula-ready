from django.contrib.gis import admin
from embed_video.admin import AdminVideoMixin
from solo.admin import SingletonModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminModelImports
from .models import EmbedSnugget, TextSnugget, SnuggetSection, SnuggetSubSection, Location, SiteSettings, SupplyKit, ImportantLink, EQ_Fault_Buffer, EQ_Fault_Shaking, EQ_Fault_Worst, EQ_Historic_Distance, Fire_Burn_Probability2, Fire_Hist_Bound, Fire_Worst_Case_ph2, Flood_Channel_Migration_Zones, Flood_FEMA_DFRIM_2015, Flood_Worst_Case, Landslide_placeholder2, summerstorm, winterstorm
# END OF GENERATED CODE BLOCK
######################################################
from .models import PastEventsPhoto, DataOverviewImage, UserProfile, ShapefileGroup
from .actions import export_as_csv_action
admin.site.register(SnuggetSection, admin.ModelAdmin)
admin.site.register(SnuggetSubSection, admin.ModelAdmin)
admin.site.register(ShapefileGroup, admin.ModelAdmin)


class SnuggetAdmin(admin.ModelAdmin):
######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminLists
    list_display = ('shortname', 'section', 'sub_section', 'EQ_Fault_Buffer_filter', 'EQ_Fault_Shaking_filter', 'EQ_Fault_Worst_filter', 'EQ_Historic_Distance_filter', 'Fire_Burn_Probability2_filter', 'Fire_Hist_Bound_filter', 'Fire_Worst_Case_ph2_filter', 'Flood_Channel_Migration_Zones_filter', 'Flood_FEMA_DFRIM_2015_filter', 'Flood_Worst_Case_filter', 'Landslide_placeholder2_filter', 'summerstorm_filter', 'winterstorm_filter')
    list_filter = ('section', 'sub_section', 'EQ_Fault_Buffer_filter', 'EQ_Fault_Shaking_filter', 'EQ_Fault_Worst_filter', 'EQ_Historic_Distance_filter', 'Fire_Burn_Probability2_filter', 'Fire_Hist_Bound_filter', 'Fire_Worst_Case_ph2_filter', 'Flood_Channel_Migration_Zones_filter', 'Flood_FEMA_DFRIM_2015_filter', 'Flood_Worst_Case_filter', 'Landslide_placeholder2_filter', 'summerstorm_filter', 'winterstorm_filter')

    fieldsets = (
        (None, {
            'fields': ('section', 'sub_section')
        }),
        ('Filters', {
            'description': 'Choose a filter value this snugget will show up for.  It is recommended you only select a value for one filter and leave the rest empty.',
            'fields': (('EQ_Fault_Buffer_filter', 'EQ_Fault_Shaking_filter', 'EQ_Fault_Worst_filter', 'EQ_Historic_Distance_filter', 'Fire_Burn_Probability2_filter', 'Fire_Hist_Bound_filter', 'Fire_Worst_Case_ph2_filter', 'Flood_Channel_Migration_Zones_filter', 'Flood_FEMA_DFRIM_2015_filter', 'Flood_Worst_Case_filter', 'Landslide_placeholder2_filter', 'summerstorm_filter', 'winterstorm_filter'))
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

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Users'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    actions = [export_as_csv_action("CSV Export", fields=('username','address1','address2','city','state','zip_code'))]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# adminSiteRegistrations
admin.site.register(EQ_Fault_Buffer, GeoNoEditAdmin)
admin.site.register(EQ_Fault_Shaking, GeoNoEditAdmin)
admin.site.register(EQ_Fault_Worst, GeoNoEditAdmin)
admin.site.register(EQ_Historic_Distance, GeoNoEditAdmin)
admin.site.register(Fire_Burn_Probability2, GeoNoEditAdmin)
admin.site.register(Fire_Hist_Bound, GeoNoEditAdmin)
admin.site.register(Fire_Worst_Case_ph2, GeoNoEditAdmin)
admin.site.register(Flood_Channel_Migration_Zones, GeoNoEditAdmin)
admin.site.register(Flood_FEMA_DFRIM_2015, GeoNoEditAdmin)
admin.site.register(Flood_Worst_Case, GeoNoEditAdmin)
admin.site.register(Landslide_placeholder2, GeoNoEditAdmin)
admin.site.register(summerstorm, GeoNoEditAdmin)
admin.site.register(winterstorm, GeoNoEditAdmin)
# END OF GENERATED CODE BLOCK
######################################################

