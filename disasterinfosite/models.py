from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import Extent
from django.db.models.signals import post_save
from embed_video.fields import EmbedVideoField
from model_utils.managers import InheritanceManager
from solo.models import SingletonModel

SNUG_TEXT = 0
SNUG_AUDIO = 1
SNUG_VID = 2

SNUGGET_TYPES = (
                 ('SNUG_TEXT', 'TextSnugget'),
                 )

class UserProfile(models.Model):
    """ A model representing a user's information that isn't their username, password, or email address """
    user = models.OneToOneField(User)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return "{0}: {1}, {2} {3}, {4} {5}".format(self.user, self.address1, self.address2, self.city, self.state, self.zip_code)


class SiteSettings(SingletonModel):
    """A singleton model to represent site-wide settings."""
    about_text = models.TextField(
        default="Information about your organization goes here.",
        help_text="Describe the data and the agencies that it came from."
    )
    contact_email = models.EmailField(
        blank=True,
        help_text="Put a contact email for the maintainer of this site here."
    )
    site_url = models.URLField(
        default="https://www.example.com",
        help_text="Put the URL to this site here."
    )
    site_title = models.CharField(
        max_length=50,
        default="Your Title Here!"
    )
    site_description = models.CharField(
        max_length=200,
        default="A disaster preparedness website",
        help_text="A small, catchy description for this site."
    )
    intro_text= models.TextField(
        default="A natural disaster could strike your area at any time.",
        help_text="A description of what we are trying to help people prepare for, or the goal of your site."
    )
    who_made_this = models.TextField(
        default="Information about the creators and maintainers of this particular site.",
        help_text="Include information about who you are and how to contact you."
    )
    data_download = models.URLField(
        blank=True,
        help_text="A link where people can download a zipfile of all the data that powers this site."
    )

    def __unicode__(self):
        return u"Site Settings"

    class Meta:
        verbose_name = "Site Settings"


class Location(SingletonModel):
    """A singleton model to represent the location covered by this website's data"""
    area_name = models.CharField(
        max_length=100,
        default="the affected area",
        help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'."
    )

    community_leaders = models.TextField(
        default="Information about community leaders goes here.",
        help_text="Information about community leaders, how to contact them, and form groups."
    )

    def __unicode__(self):
        return u"Location Information"

    @staticmethod
    def get_data_bounds():
        bounds = {
    ######################################################
    # GENERATED CODE GOES HERE
    # DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
    # locationsList
            'Fire_Burn_Probability2': Fire_Burn_Probability2.objects.data_bounds(),
            'Flood_Worst_Case': Flood_Worst_Case.objects.data_bounds(),
            'EQ_Fault_Buffer': EQ_Fault_Buffer.objects.data_bounds(),
            'Fire_Worst_Case_ph2': Fire_Worst_Case_ph2.objects.data_bounds(),
            'EQ_Fault_Worst': EQ_Fault_Worst.objects.data_bounds(),
            'EQ_Historic_Distance': EQ_Historic_Distance.objects.data_bounds(),
            'EQ_Fault_Shaking': EQ_Fault_Shaking.objects.data_bounds(),
            'Flood_FEMA_DFRIM_2015': Flood_FEMA_DFRIM_2015.objects.data_bounds(),
            'Fire_Hist_Bound': Fire_Hist_Bound.objects.data_bounds(),
            'winterstorm': winterstorm.objects.data_bounds(),
            'summerstorm': summerstorm.objects.data_bounds(),
            'Landslide_placeholder2': Landslide_placeholder2.objects.data_bounds(),
            'Flood_Channel_Migration_Zones': Flood_Channel_Migration_Zones.objects.data_bounds()
    # END OF GENERATED CODE BLOCK
    ######################################################
        }

        # The smallest/largest possible values, as appropriate, so the map will display
        # something if there is no data
        north = [-80]
        west = [180]
        south = [80]
        east = [-180]

        for box in bounds.values():
            west.append(box[0])
            south.append(box[1])
            east.append(box[2])
            north.append(box[3])

        # The largest box that contains all the bounding boxes, how Leaflet wants it.
        return [[min(south), min(west)], [max(north), max(east)]]


    class Meta:
        verbose_name = "Location Information"

class SupplyKit(SingletonModel):
    """ A singleton model representing the supply kit information """
    days = models.PositiveIntegerField(
        default=3,
        help_text="The number of days' worth of supplies prepared residents should have on hand."
    )
    text = models.TextField(
        help_text="More information about building your supply kit. Any web address in here gets turned into a link automatically."
    )

class ImportantLink(models.Model):
    """ A model representing a link with a title """
    title = models.CharField(
        max_length=50,
        help_text="A title for your important link, like 'Evacuation Information'"
    )
    link = models.TextField(
        help_text="Your link and any information about it. You can use HTML in here, and it'll render correctly."
    )
    def __str__(self):
        return self.title +': ' + self.link

class ShapeManager(models.GeoManager):
    def has_point(self, pnt):
        return self.filter(geom__contains=pnt)

    def data_bounds(self):
        return self.aggregate(Extent('geom'))['geom__extent']

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsClasses
class Fire_Burn_Probability2(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class Flood_Worst_Case(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class EQ_Fault_Buffer(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class Fire_Worst_Case_ph2(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class EQ_Fault_Worst(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class EQ_Historic_Distance(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class EQ_Fault_Shaking(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class Flood_FEMA_DFRIM_2015(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class Fire_Hist_Bound(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class winterstorm(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class summerstorm(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class Landslide_placeholder2(models.Model):
    lookup_val = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

class Flood_Channel_Migration_Zones(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    def __str__(self):
        return str(self.lookup_val)

# END OF GENERATED CODE BLOCK
######################################################

class RecoveryLevels(models.Model):
    name = models.CharField(max_length=50)
    shortLabel = models.CharField(max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Infrastructure(models.Model):
    name = models.CharField(max_length=255)
    eventOccursRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    firstDayRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threeDaysRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    sevenDaysRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    fourWeeksRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threeMonthsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    sixMonthsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    twelveMonthsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threeYearsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)
    threePlusYearsRecovery = models.ForeignKey(RecoveryLevels, related_name='+', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name + " in " + str(self.zone)


class InfrastructureGroup(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Infrastructure)

    def __str__(self):
        return self.name


class InfrastructureCategory(models.Model):
    name = models.CharField(max_length=50)
    groups = models.ManyToManyField(InfrastructureGroup)

    def __str__(self):
        return self.name + " in " + str(self.zone)


class SnuggetType(models.Model):
    name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=255, choices=SNUGGET_TYPES)

    def __str__(self):
        return self.name


class SnuggetSection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SnuggetSubSection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Snugget(models.Model):
    objects = InheritanceManager()

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsFilters
    Fire_Burn_Probability2_filter = models.ForeignKey(Fire_Burn_Probability2, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Flood_Worst_Case_filter = models.ForeignKey(Flood_Worst_Case, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQ_Fault_Buffer_filter = models.ForeignKey(EQ_Fault_Buffer, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Fire_Worst_Case_ph2_filter = models.ForeignKey(Fire_Worst_Case_ph2, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQ_Fault_Worst_filter = models.ForeignKey(EQ_Fault_Worst, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQ_Historic_Distance_filter = models.ForeignKey(EQ_Historic_Distance, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    EQ_Fault_Shaking_filter = models.ForeignKey(EQ_Fault_Shaking, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Flood_FEMA_DFRIM_2015_filter = models.ForeignKey(Flood_FEMA_DFRIM_2015, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Fire_Hist_Bound_filter = models.ForeignKey(Fire_Hist_Bound, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    winterstorm_filter = models.ForeignKey(winterstorm, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    summerstorm_filter = models.ForeignKey(summerstorm, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Landslide_placeholder2_filter = models.ForeignKey(Landslide_placeholder2, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Flood_Channel_Migration_Zones_filter = models.ForeignKey(Flood_Channel_Migration_Zones, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
# END OF GENERATED CODE BLOCK
######################################################

    section = models.ForeignKey(SnuggetSection, related_name='+', on_delete=models.PROTECT)
    sub_section = models.ForeignKey(SnuggetSubSection, related_name='+', on_delete=models.PROTECT, null=True, blank=True)

    def getRelatedTemplate(self):
        return "snugget.html"

    @staticmethod
    def findSnuggetsForPoint(lat=0, lng=0, merge_deform = True):
        pnt = Point(lng, lat)



######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsGeoFilters

        fire_snuggets = []
        flood_snuggets = []
        quake_snuggets = []
        winterstorm_snuggets = []
        summerstorm_snuggets = []
        Landslide_placeholder2_snuggets = []

        qs_Fire_Burn_Probability2 = Fire_Burn_Probability2.objects.filter(geom__contains=pnt)
        Fire_Burn_Probability2_rating = qs_Fire_Burn_Probability2.values_list('lookup_val', flat=True)
        for rating in Fire_Burn_Probability2_rating:
            individualSnugget = Snugget.objects.filter(Fire_Burn_Probability2_filter__lookup_val__exact=rating).select_subclasses()
            fire_snuggets.extend(individualSnugget)

        qs_Flood_Worst_Case = Flood_Worst_Case.objects.filter(geom__contains=pnt)
        Flood_Worst_Case_rating = qs_Flood_Worst_Case.values_list('lookup_val', flat=True)
        for rating in Flood_Worst_Case_rating:
            individualSnugget = Snugget.objects.filter(Flood_Worst_Case_filter__lookup_val__exact=rating).select_subclasses()
            flood_snuggets.extend(individualSnugget)

        qs_EQ_Fault_Buffer = EQ_Fault_Buffer.objects.filter(geom__contains=pnt)
        EQ_Fault_Buffer_rating = qs_EQ_Fault_Buffer.values_list('lookup_val', flat=True)
        for rating in EQ_Fault_Buffer_rating:
            individualSnugget = Snugget.objects.filter(EQ_Fault_Buffer_filter__lookup_val__exact=rating).select_subclasses()
            quake_snuggets.extend(individualSnugget)

        qs_Fire_Worst_Case_ph2 = Fire_Worst_Case_ph2.objects.filter(geom__contains=pnt)
        Fire_Worst_Case_ph2_rating = qs_Fire_Worst_Case_ph2.values_list('lookup_val', flat=True)
        for rating in Fire_Worst_Case_ph2_rating:
            individualSnugget = Snugget.objects.filter(Fire_Worst_Case_ph2_filter__lookup_val__exact=rating).select_subclasses()
            fire_snuggets.extend(individualSnugget)

        qs_EQ_Fault_Worst = EQ_Fault_Worst.objects.filter(geom__contains=pnt)
        EQ_Fault_Worst_rating = qs_EQ_Fault_Worst.values_list('lookup_val', flat=True)
        for rating in EQ_Fault_Worst_rating:
            individualSnugget = Snugget.objects.filter(EQ_Fault_Worst_filter__lookup_val__exact=rating).select_subclasses()
            quake_snuggets.extend(individualSnugget)

        qs_EQ_Historic_Distance = EQ_Historic_Distance.objects.filter(geom__contains=pnt)
        EQ_Historic_Distance_rating = qs_EQ_Historic_Distance.values_list('lookup_val', flat=True)
        for rating in EQ_Historic_Distance_rating:
            individualSnugget = Snugget.objects.filter(EQ_Historic_Distance_filter__lookup_val__exact=rating).select_subclasses()
            quake_snuggets.extend(individualSnugget)

        qs_EQ_Fault_Shaking = EQ_Fault_Shaking.objects.filter(geom__contains=pnt)
        EQ_Fault_Shaking_rating = qs_EQ_Fault_Shaking.values_list('lookup_val', flat=True)
        for rating in EQ_Fault_Shaking_rating:
            individualSnugget = Snugget.objects.filter(EQ_Fault_Shaking_filter__lookup_val__exact=rating).select_subclasses()
            quake_snuggets.extend(individualSnugget)

        qs_Flood_FEMA_DFRIM_2015 = Flood_FEMA_DFRIM_2015.objects.filter(geom__contains=pnt)
        Flood_FEMA_DFRIM_2015_rating = qs_Flood_FEMA_DFRIM_2015.values_list('lookup_val', flat=True)
        for rating in Flood_FEMA_DFRIM_2015_rating:
            individualSnugget = Snugget.objects.filter(Flood_FEMA_DFRIM_2015_filter__lookup_val__exact=rating).select_subclasses()
            flood_snuggets.extend(individualSnugget)

        qs_Fire_Hist_Bound = Fire_Hist_Bound.objects.filter(geom__contains=pnt)
        Fire_Hist_Bound_rating = qs_Fire_Hist_Bound.values_list('lookup_val', flat=True)
        for rating in Fire_Hist_Bound_rating:
            individualSnugget = Snugget.objects.filter(Fire_Hist_Bound_filter__lookup_val__exact=rating).select_subclasses()
            fire_snuggets.extend(individualSnugget)

        qs_winterstorm = winterstorm.objects.filter(geom__contains=pnt)
        winterstorm_rating = qs_winterstorm.values_list('lookup_val', flat=True)
        for rating in winterstorm_rating:
            individualSnugget = Snugget.objects.filter(winterstorm_filter__lookup_val__exact=rating).select_subclasses()
            winterstorm_snuggets.extend(individualSnugget)

        qs_summerstorm = summerstorm.objects.filter(geom__contains=pnt)
        summerstorm_rating = qs_summerstorm.values_list('lookup_val', flat=True)
        for rating in summerstorm_rating:
            individualSnugget = Snugget.objects.filter(summerstorm_filter__lookup_val__exact=rating).select_subclasses()
            summerstorm_snuggets.extend(individualSnugget)

        qs_Landslide_placeholder2 = Landslide_placeholder2.objects.filter(geom__contains=pnt)
        Landslide_placeholder2_rating = qs_Landslide_placeholder2.values_list('lookup_val', flat=True)
        for rating in Landslide_placeholder2_rating:
            individualSnugget = Snugget.objects.filter(Landslide_placeholder2_filter__lookup_val__exact=rating).select_subclasses()
            Landslide_placeholder2_snuggets.extend(individualSnugget)

        qs_Flood_Channel_Migration_Zones = Flood_Channel_Migration_Zones.objects.filter(geom__contains=pnt)
        Flood_Channel_Migration_Zones_rating = qs_Flood_Channel_Migration_Zones.values_list('lookup_val', flat=True)
        for rating in Flood_Channel_Migration_Zones_rating:
            individualSnugget = Snugget.objects.filter(Flood_Channel_Migration_Zones_filter__lookup_val__exact=rating).select_subclasses()
            flood_snuggets.extend(individualSnugget)


        return {'groups': {
                          'fire_snugs': fire_snuggets,
                          'flood_snugs': flood_snuggets,
                          'quake_snugs': quake_snuggets,
                          'winterstorm_snugs': winterstorm_snuggets,
                          'summerstorm_snugs': summerstorm_snuggets,
                          'Landslide_placeholder2_snugs': Landslide_placeholder2_snuggets
                          },
                'Fire_Burn_Probability2_rating': Fire_Burn_Probability2_rating,
                'Flood_Worst_Case_rating': Flood_Worst_Case_rating,
                'EQ_Fault_Buffer_rating': EQ_Fault_Buffer_rating,
                'Fire_Worst_Case_ph2_rating': Fire_Worst_Case_ph2_rating,
                'EQ_Fault_Worst_rating': EQ_Fault_Worst_rating,
                'EQ_Historic_Distance_rating': EQ_Historic_Distance_rating,
                'EQ_Fault_Shaking_rating': EQ_Fault_Shaking_rating,
                'Flood_FEMA_DFRIM_2015_rating': Flood_FEMA_DFRIM_2015_rating,
                'Fire_Hist_Bound_rating': Fire_Hist_Bound_rating,
                'winterstorm_rating': winterstorm_rating,
                'summerstorm_rating': summerstorm_rating,
                'Landslide_placeholder2_rating': Landslide_placeholder2_rating,
                'Flood_Channel_Migration_Zones_rating': Flood_Channel_Migration_Zones_rating
                }
# END OF GENERATED CODE BLOCK
######################################################


    def __str__(self):
        return "Snugget base class string."


class TextSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_TEXT]
    content = models.TextField()
    heading = models.TextField(default="")
    image = models.TextField(default="")
    percentage = models.FloatField(null=True)

    def getRelatedTemplate(self):
        return "snugget_text.html"

    def __str__(self):
        return str(self.content)[:100]


class EmbedSnugget(Snugget):
    embed = EmbedVideoField()

    def getRelatedTemplate(self):
        return "snugget_embed.html"

    def __str__(self):
        return "Embed Snugget: " + str(self.embed)

class PastEventsPhoto(models.Model):
    heading = models.CharField(default="", max_length=50)
    image = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.image.url

class DataOverviewImage(models.Model):
    link_text = models.CharField(default="", max_length=100)
    image = models.ImageField(upload_to="data")

    def __str__(self):
        return self.image.url
