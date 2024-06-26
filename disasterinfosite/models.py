from collections import OrderedDict
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import Extent
from embed_video.fields import EmbedVideoField
from model_utils.managers import InheritanceManager
from solo.models import SingletonModel
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.postgres.validators import (
    RangeMinValueValidator, RangeMaxValueValidator)


SNUG_TEXT = 0
SNUG_VIDEO = 1
SNUG_SLIDESHOW = 2

SNUGGET_TYPES = (
    ('SNUG_TEXT', 'TextSnugget'),
    ('SNUG_VIDEO', 'EmbedSnugget'),
    ('SNUG_SLIDESHOW', 'SlideshowSnugget')
)


class PreparednessAction(models.Model):
    title = models.TextField(default="")
    image = models.ImageField(upload_to="prepare_images")
    cost = models.IntegerField(default=0,
                               validators=[
                                   RangeMinValueValidator(0),
                                   RangeMaxValueValidator(4)
                               ])
    happy_text = models.TextField(default="")
    useful_text = models.TextField(default="")
    property_text = models.TextField(default="")
    content_text = models.TextField(default="")
    link_icon = models.ImageField(upload_to="prepare_images")
    slug = models.TextField(default="")

    def __str__(self):
        return self.title


class PreparednessLink(models.Model):
    text = models.TextField(default="")
    url = models.URLField(default="")
    action = models.ForeignKey(PreparednessAction, on_delete=models.CASCADE)

    def __str__(self):
        return self.text + "(" + self.url + ") action: " + self.action


class UserProfile(models.Model):
    """ A model representing a user's information that isn't their
    username, password, or email address """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)
    actions_taken = models.ManyToManyField(PreparednessAction, blank=True)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return "{0}: {1}, {2} {3}, {4} {5}: {6}".format(
            self.user,
            self.address1,
            self.address2,
            self.city,
            self.state,
            self.zip_code,
            self.actions_taken.all().values_list('title', flat=True)
        )


class SiteSettings(SingletonModel):
    """A singleton model to represent site-wide settings."""
    area_name = models.CharField(
        max_length=100,
        default="the affected area",
        help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'."  # noqa: ES501
    )
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
    intro_text = models.TextField(
        default="A natural disaster could strike your area at any time.",
        help_text="A description of what we are trying to help people prepare for, or the goal of your site."  # noqa: ES501
    )
    who_made_this = models.TextField(
        default="Information about the creators and maintainers of this particular site.",  # noqa: ES501
        help_text="Include information about who you are and how to contact you."  # noqa: ES501
    )
    data_download = models.URLField(
        blank=True,
        help_text="A link where people can download a zipfile of all the data that powers this site."  # noqa: ES501
    )

    def __unicode__(self):
        return u"Site Settings"

    class Meta:
        verbose_name = "Site Settings"


class Location(SingletonModel):
    """A singleton model to represent the location
    covered by this website's data"""

    def __unicode__(self):
        return u"Location Information"

    @staticmethod
    def get_data_bounds():
        bounds = {
            ######################################################
            # GENERATED CODE GOES HERE
            # DO NOT MANUALLY EDIT CODE IN THIS SECTION- IT WILL BE OVERWRITTEN
            # locationsList
            'Ravalli_co': Ravalli_co.objects.data_bounds(),
            'Silverbow_co': Silverbow_co.objects.data_bounds(),
            'AllCounties': AllCounties.objects.data_bounds(),
            'fire_wui_wmt': fire_wui_wmt.objects.data_bounds(),
            'Burned_perimeter': Burned_perimeter.objects.data_bounds(),
            'WHP_FINAL': WHP_FINAL.objects.data_bounds(),
            'DeerLodge_co': DeerLodge_co.objects.data_bounds(),
            'Missoula_co': Missoula_co.objects.data_bounds(),
            'Granite_co': Granite_co.objects.data_bounds(),
            'Flathead_co': Flathead_co.objects.data_bounds(),
            'Beaverhead_co': Beaverhead_co.objects.data_bounds(),
            'Gallatin_co': Gallatin_co.objects.data_bounds(),
            'Lincoln_co': Lincoln_co.objects.data_bounds(),
            'MergedEQs': MergedEQs.objects.data_bounds(),
            'Mineral_co': Mineral_co.objects.data_bounds(),
            'FloodMaps_MT': FloodMaps_MT.objects.data_bounds(),
            'Lake_co': Lake_co.objects.data_bounds(),
            'Sanders_co': Sanders_co.objects.data_bounds(),
            'Madison_co': Madison_co.objects.data_bounds(),
            'CMZ_mt': CMZ_mt.objects.data_bounds()
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
            if box is not None:
                west.append(box[0])
                south.append(box[1])
                east.append(box[2])
                north.append(box[3])

        # The largest box that contains all the bounding boxes,
        # how Leaflet wants it.
        return [[min(south), min(west)], [max(north), max(east)]]

    class Meta:
        verbose_name = "Location Information"


class ShapeManager(models.Manager):
    def data_bounds(self):
        return self.aggregate(Extent('geom'))['geom__extent']


class RasterManager(models.Manager):
    def data_bounds(self):
        return self.aggregate(Extent('bbox'))['bbox__extent']


class ShapefileGroup(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50, default="")
    order_of_appearance = models.IntegerField(
        default=0,
        help_text="The order, from top to bottom, in which you would like this group to appear, when applicable."  # noqa: ES501
    )
    note = models.TextField(
        blank=True,
        help_text='A note that appears above all snuggets in this section. Use for data caveats or warnings.'  # noqa: ES501
    )

    def __str__(self):
        return self.name

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsClasses
class Ravalli_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Silverbow_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class AllCounties(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class fire_wui_wmt(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Burned_perimeter(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class WHP_FINAL(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class DeerLodge_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Missoula_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Granite_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Flathead_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Beaverhead_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Gallatin_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Lincoln_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class MergedEQs(models.Model):
    lookup_val = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Mineral_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class FloodMaps_MT(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Lake_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Sanders_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class Madison_co(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

class CMZ_mt(models.Model):
    lookup_val = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    objects = ShapeManager()

    groups = models.ManyToManyField(ShapefileGroup)
    def __str__(self):
        return str(self.lookup_val)

# END OF GENERATED CODE BLOCK
######################################################


class SnuggetType(models.Model):
    name = models.CharField(max_length=50)
    model_name = models.CharField(max_length=255, choices=SNUGGET_TYPES)

    def __str__(self):
        return self.name


class SnuggetSection(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(
        max_length=100,
        help_text="The name to show for this section",
        default=""
    )
    collapsible = models.BooleanField(
        default=True,
        help_text='Whether this section of the data is collapsible'
    )
    order_of_appearance = models.IntegerField(
        default=0,
        help_text="The order in which you'd like this to appear in the tab. 0 is at the top."  # noqa: ES501
    )

    def __str__(self):
        return self.name


class SnuggetPopOut(models.Model):
    text = models.TextField(default='')
    image = models.ImageField(upload_to="popout_images")
    link = models.TextField(default='', max_length=255)
    alt_text = models.TextField(default='', max_length=255)
    video = EmbedVideoField(null=True)

    @property
    def has_content(self):
        "Returns true if this popout has some content"
        return (self.text or self.image or self.link or self.video)

    def __str__(self):
        return self.text[:100]


@receiver(pre_save, sender=SnuggetSection)
@receiver(pre_save, sender=ShapefileGroup)
def default_display_name(sender, instance, *args, **kwargs):
    if not instance.display_name:
        instance.display_name = instance.name


"""
looks up a point in a set of rasters and returns the first non-NODATA value it finds
 or None if there are no rasters, the point is not within any of them or it's in a NODATA pixel.
 raster algebra taken from the django-raster project version 0.6 at
 https://github.com/geodesign/django-raster/blob/master/raster/utils.py
 """


def rasterPointLookup(rasterCollection, lng, lat, band=0):
    # if we have no data at all, then save time and return None immediately
    sampleBBOX = rasterCollection.objects.only("bbox").first().bbox
    if sampleBBOX is None:
        return None

    rasterPoint = OGRGeometry(
        'POINT({0} {1})'.format(lng, lat), srs=sampleBBOX.srs)
    vectorPoint = Point(lng, lat, srid=sampleBBOX.srid)

    """ Using the filter here lets PostGIS do an indexed search on the bbox
    field, which is much faster than stepping through the objects.
    Note that it will almost always only return one raster, but there could
    theoretically be 2 or 4 if our point is perfectly on a tile boundary.
    In that instance, we return the first non-NODATA value we find.
    """
    for tile in rasterCollection.objects.filter(
            bbox__contains=vectorPoint).all():
        # only bother to check for data if we're within the bounds
        rst = tile.rast
        offset = (
            abs(rst.origin.x - rasterPoint.coords[0]),
            abs(rst.origin.y - rasterPoint.coords[1])
        )
        offset_idx = [int(offset[0] / abs(rst.scale.x)),
                      int(offset[1] / abs(rst.scale.y))]

        # points very close to the boundary can get
        # rounded to 1 pixel beyond it, so fix that here
        if offset_idx[0] == rst.width:
            offset_idx[0] -= 1
        if offset_idx[1] == rst.height:
            offset_idx[1] -= 1

        result = rst.bands[band].data(offset=offset_idx, size=(1, 1))[0]
        if result != rst.bands[band].nodata_value:
            return rst.bands[band].data(offset=offset_idx, size=(1, 1))[0]

    return None


class Snugget(models.Model):
    objects = InheritanceManager()

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsFilters
    Ravalli_co_filter = models.ForeignKey(Ravalli_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Silverbow_co_filter = models.ForeignKey(Silverbow_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    AllCounties_filter = models.ForeignKey(AllCounties, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    fire_wui_wmt_filter = models.ForeignKey(fire_wui_wmt, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Burned_perimeter_filter = models.ForeignKey(Burned_perimeter, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    WHP_FINAL_filter = models.ForeignKey(WHP_FINAL, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    DeerLodge_co_filter = models.ForeignKey(DeerLodge_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Missoula_co_filter = models.ForeignKey(Missoula_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Granite_co_filter = models.ForeignKey(Granite_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Flathead_co_filter = models.ForeignKey(Flathead_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Beaverhead_co_filter = models.ForeignKey(Beaverhead_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Gallatin_co_filter = models.ForeignKey(Gallatin_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Lincoln_co_filter = models.ForeignKey(Lincoln_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    MergedEQs_filter = models.ForeignKey(MergedEQs, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Mineral_co_filter = models.ForeignKey(Mineral_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    FloodMaps_MT_filter = models.ForeignKey(FloodMaps_MT, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Lake_co_filter = models.ForeignKey(Lake_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Sanders_co_filter = models.ForeignKey(Sanders_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    Madison_co_filter = models.ForeignKey(Madison_co, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
    CMZ_mt_filter = models.ForeignKey(CMZ_mt, related_name='+', on_delete=models.PROTECT, blank=True, null=True)
# END OF GENERATED CODE BLOCK
######################################################

    section = models.ForeignKey(
        SnuggetSection, related_name='+', on_delete=models.PROTECT)
    group = models.ForeignKey(
        ShapefileGroup, on_delete=models.PROTECT, null=True)
    pop_out = models.OneToOneField(
        SnuggetPopOut, on_delete=models.PROTECT, blank=True, null=True)
    percentage = models.FloatField(null=True)
    order = models.IntegerField(default=0)

    def getRelatedTemplate(self):
        return "snugget.html"

    @staticmethod
    def findSnuggetsForPoint(lat=0, lng=0, merge_deform=True):
        pnt = Point(lng, lat)
        groups = ShapefileGroup.objects.all().order_by('order_of_appearance')
        groupsDict = OrderedDict({el: [] for el in groups})

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# modelsGeoFilters
        qs_Ravalli_co = Ravalli_co.objects.filter(geom__contains=pnt)
        Ravalli_co_rating = qs_Ravalli_co.values_list('lookup_val', flat=True)
        for rating in Ravalli_co_rating:
            Ravalli_co_snuggets = Snugget.objects.filter(Ravalli_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Ravalli_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Silverbow_co = Silverbow_co.objects.filter(geom__contains=pnt)
        Silverbow_co_rating = qs_Silverbow_co.values_list('lookup_val', flat=True)
        for rating in Silverbow_co_rating:
            Silverbow_co_snuggets = Snugget.objects.filter(Silverbow_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Silverbow_co_snuggets:
                groupsDict[s.group].append(s)

        qs_AllCounties = AllCounties.objects.filter(geom__contains=pnt)
        AllCounties_rating = qs_AllCounties.values_list('lookup_val', flat=True)
        for rating in AllCounties_rating:
            AllCounties_snuggets = Snugget.objects.filter(AllCounties_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in AllCounties_snuggets:
                groupsDict[s.group].append(s)

        qs_fire_wui_wmt = fire_wui_wmt.objects.filter(geom__contains=pnt)
        fire_wui_wmt_rating = qs_fire_wui_wmt.values_list('lookup_val', flat=True)
        for rating in fire_wui_wmt_rating:
            fire_wui_wmt_snuggets = Snugget.objects.filter(fire_wui_wmt_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in fire_wui_wmt_snuggets:
                groupsDict[s.group].append(s)

        qs_Burned_perimeter = Burned_perimeter.objects.filter(geom__contains=pnt)
        Burned_perimeter_rating = qs_Burned_perimeter.values_list('lookup_val', flat=True)
        for rating in Burned_perimeter_rating:
            Burned_perimeter_snuggets = Snugget.objects.filter(Burned_perimeter_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Burned_perimeter_snuggets:
                groupsDict[s.group].append(s)

        qs_WHP_FINAL = WHP_FINAL.objects.filter(geom__contains=pnt)
        WHP_FINAL_rating = qs_WHP_FINAL.values_list('lookup_val', flat=True)
        for rating in WHP_FINAL_rating:
            WHP_FINAL_snuggets = Snugget.objects.filter(WHP_FINAL_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in WHP_FINAL_snuggets:
                groupsDict[s.group].append(s)

        qs_DeerLodge_co = DeerLodge_co.objects.filter(geom__contains=pnt)
        DeerLodge_co_rating = qs_DeerLodge_co.values_list('lookup_val', flat=True)
        for rating in DeerLodge_co_rating:
            DeerLodge_co_snuggets = Snugget.objects.filter(DeerLodge_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in DeerLodge_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Missoula_co = Missoula_co.objects.filter(geom__contains=pnt)
        Missoula_co_rating = qs_Missoula_co.values_list('lookup_val', flat=True)
        for rating in Missoula_co_rating:
            Missoula_co_snuggets = Snugget.objects.filter(Missoula_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Missoula_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Granite_co = Granite_co.objects.filter(geom__contains=pnt)
        Granite_co_rating = qs_Granite_co.values_list('lookup_val', flat=True)
        for rating in Granite_co_rating:
            Granite_co_snuggets = Snugget.objects.filter(Granite_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Granite_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Flathead_co = Flathead_co.objects.filter(geom__contains=pnt)
        Flathead_co_rating = qs_Flathead_co.values_list('lookup_val', flat=True)
        for rating in Flathead_co_rating:
            Flathead_co_snuggets = Snugget.objects.filter(Flathead_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Flathead_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Beaverhead_co = Beaverhead_co.objects.filter(geom__contains=pnt)
        Beaverhead_co_rating = qs_Beaverhead_co.values_list('lookup_val', flat=True)
        for rating in Beaverhead_co_rating:
            Beaverhead_co_snuggets = Snugget.objects.filter(Beaverhead_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Beaverhead_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Gallatin_co = Gallatin_co.objects.filter(geom__contains=pnt)
        Gallatin_co_rating = qs_Gallatin_co.values_list('lookup_val', flat=True)
        for rating in Gallatin_co_rating:
            Gallatin_co_snuggets = Snugget.objects.filter(Gallatin_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Gallatin_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Lincoln_co = Lincoln_co.objects.filter(geom__contains=pnt)
        Lincoln_co_rating = qs_Lincoln_co.values_list('lookup_val', flat=True)
        for rating in Lincoln_co_rating:
            Lincoln_co_snuggets = Snugget.objects.filter(Lincoln_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Lincoln_co_snuggets:
                groupsDict[s.group].append(s)

        qs_MergedEQs = MergedEQs.objects.filter(geom__contains=pnt)
        MergedEQs_rating = qs_MergedEQs.values_list('lookup_val', flat=True)
        for rating in MergedEQs_rating:
            MergedEQs_snuggets = Snugget.objects.filter(MergedEQs_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in MergedEQs_snuggets:
                groupsDict[s.group].append(s)

        qs_Mineral_co = Mineral_co.objects.filter(geom__contains=pnt)
        Mineral_co_rating = qs_Mineral_co.values_list('lookup_val', flat=True)
        for rating in Mineral_co_rating:
            Mineral_co_snuggets = Snugget.objects.filter(Mineral_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Mineral_co_snuggets:
                groupsDict[s.group].append(s)

        qs_FloodMaps_MT = FloodMaps_MT.objects.filter(geom__contains=pnt)
        FloodMaps_MT_rating = qs_FloodMaps_MT.values_list('lookup_val', flat=True)
        for rating in FloodMaps_MT_rating:
            FloodMaps_MT_snuggets = Snugget.objects.filter(FloodMaps_MT_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in FloodMaps_MT_snuggets:
                groupsDict[s.group].append(s)

        qs_Lake_co = Lake_co.objects.filter(geom__contains=pnt)
        Lake_co_rating = qs_Lake_co.values_list('lookup_val', flat=True)
        for rating in Lake_co_rating:
            Lake_co_snuggets = Snugget.objects.filter(Lake_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Lake_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Sanders_co = Sanders_co.objects.filter(geom__contains=pnt)
        Sanders_co_rating = qs_Sanders_co.values_list('lookup_val', flat=True)
        for rating in Sanders_co_rating:
            Sanders_co_snuggets = Snugget.objects.filter(Sanders_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Sanders_co_snuggets:
                groupsDict[s.group].append(s)

        qs_Madison_co = Madison_co.objects.filter(geom__contains=pnt)
        Madison_co_rating = qs_Madison_co.values_list('lookup_val', flat=True)
        for rating in Madison_co_rating:
            Madison_co_snuggets = Snugget.objects.filter(Madison_co_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in Madison_co_snuggets:
                groupsDict[s.group].append(s)

        qs_CMZ_mt = CMZ_mt.objects.filter(geom__contains=pnt)
        CMZ_mt_rating = qs_CMZ_mt.values_list('lookup_val', flat=True)
        for rating in CMZ_mt_rating:
            CMZ_mt_snuggets = Snugget.objects.filter(CMZ_mt_filter__lookup_val__exact=rating).order_by('order').select_subclasses()
            for s in CMZ_mt_snuggets:
                groupsDict[s.group].append(s)

# END OF GENERATED CODE BLOCK
######################################################
        return groupsDict

    def __str__(self):
        return "Snugget base class string."


class TextSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_TEXT]
    content = models.TextField()

    def getRelatedTemplate(self):
        return "snugget_text.html"

    def __str__(self):
        return str(self.content)[:100]


class EmbedSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_VIDEO]
    text = models.TextField(default="")
    video = EmbedVideoField()

    def getRelatedTemplate(self):
        return "snugget_embed.html"

    def __str__(self):
        return "Embed Snugget: " + str(self.video)


class SlideshowSnugget(Snugget):
    name = SNUGGET_TYPES[SNUG_SLIDESHOW]
    text = models.TextField(default="")

    def getRelatedTemplate(self):
        return "snugget_slideshow.html"

    def __str__(self):
        return "Slideshow Snugget: " + str(self.text)


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


class PastEventsPhoto(models.Model):
    snugget = models.ForeignKey(
        SlideshowSnugget, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="photos", storage=OverwriteStorage())
    caption = models.TextField(default="", max_length=200)

    def __str__(self):
        return str(self.image.url) + ' Caption: ' + str(self.caption)


class DataOverviewImage(models.Model):
    link_text = models.CharField(default="", max_length=100)
    image = models.ImageField(upload_to="data", storage=OverwriteStorage())
    pdf = models.FileField(
        upload_to="data", storage=OverwriteStorage(), null=True)

    def __str__(self):
        return self.image.url
