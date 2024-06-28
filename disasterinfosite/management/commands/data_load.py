import math
import os
import sys
from django.contrib.gis.gdal import GDALRaster
from django.contrib.gis.geos import Polygon
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand
from disasterinfosite.settings import BASE_DIR

# The width & height to tile rasters to.
# Empirically, tile sizes as large as 8053 work, while 10000 hits a memory overflow bug in either Django or GDAL and crashes.
# However, smaller tiles give us faster lookups, while really small (e.g. 10) make the data load interminably slow.
rasterTileSize = 128


######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadMappings
Ravalli_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Silverbow_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

AllCounties_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

fire_wui_wmt_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Burned_perimeter_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

WHP_FINAL_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

DeerLodge_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Missoula_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Granite_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flathead_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Beaverhead_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Gallatin_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Lincoln_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

MergedEQs_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Mineral_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

FloodMaps_MT_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Lake_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Sanders_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Madison_co_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

CMZ_mt_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}


Ravalli_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Ravalli_co.shp'))
Silverbow_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Silverbow_co.shp'))
AllCounties_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/AllCounties.shp'))
fire_wui_wmt_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/fire_wui_wmt.shp'))
Burned_perimeter_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Burned_perimeter.shp'))
WHP_FINAL_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/WHP_FINAL.shp'))
DeerLodge_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/DeerLodge_co.shp'))
Missoula_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Missoula_co.shp'))
Granite_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Granite_co.shp'))
Flathead_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Flathead_co.shp'))
Beaverhead_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Beaverhead_co.shp'))
Gallatin_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Gallatin_co.shp'))
Lincoln_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Lincoln_co.shp'))
MergedEQs_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/MergedEQs.shp'))
Mineral_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Mineral_co.shp'))
FloodMaps_MT_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/FloodMaps_MT.shp'))
Lake_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Lake_co.shp'))
Sanders_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Sanders_co.shp'))
Madison_co_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/Madison_co.shp'))
CMZ_mt_shp = os.path.abspath(os.path.join(os.path.dirname(BASE_DIR), 'disasterinfosite/data/simplified/CMZ_mt.shp'))
# END OF GENERATED CODE BLOCK
######################################################

def tileLoadRaster(model, filename, shapefileGroups, band=0):
    tilesLoaded = 0
    tilesSkipped = 0
    model.objects.all().delete()
    sourceRaster = GDALRaster(filename, write=True)
    xTiles = math.ceil(sourceRaster.width / rasterTileSize)
    yTiles = math.ceil(sourceRaster.height / rasterTileSize)
    for x in range(0, xTiles):
        if x+1 != xTiles:
            width = rasterTileSize
        else:
            width = sourceRaster.width % rasterTileSize
        offsetX = x * rasterTileSize
        originX = sourceRaster.origin.x + offsetX * sourceRaster.scale.x
        for y in range(0, yTiles):
            if y+1 != yTiles:
                height = rasterTileSize
            else:
                height = sourceRaster.height % rasterTileSize
            offsetY = y * rasterTileSize
            originY = sourceRaster.origin.y + offsetY * sourceRaster.scale.y
            rasterTile = model(
                rast=GDALRaster({
                    'name': '/vsimem/tempraster',
                    'srid': sourceRaster.srid,
                    'width': width,
                    'height': height,
                    'origin': [originX, originY],
                    'scale': sourceRaster.scale,
                    'skew': sourceRaster.skew,
                    'bands': [{
                        'nodata_value': sourceRaster.bands[band].nodata_value,
                        'data': sourceRaster.bands[band].data(
                            offset=(offsetX, offsetY),
                            size=(width, height)
                        ),
                        'size': (width, height),
                        'offset': (0, 0)
                    }],
                    'datatype': 1  # GDT_Byte aka 8-bit unsigned integer
                })
            )
            if rasterTile.rast.bands[band].min is None:
                # This situation causes GDAL to print 2 lines of error code to the console, which are always safe to ignore, so we can use ANSI escape sequences to clean that up
                sys.stdout.write("\033[F\033[K")
                print("Skipping tile (" + str(x) + ", " + str(y) + ")\twith origin (" + str(originX)[:9] + ", " + str(originY)[
                      :9] + ")\tdue to lack of data. It's safe to ignore 'no valid pixels' GDAL_ERRORs in conjunction with this.")
                sys.stdout.write("\033[F\033[F\033[K")
                tilesSkipped += 1
            else:
                if y % 10 == 0:
                    sys.stdout.write('.')
                rasterTile.bbox = Polygon.from_bbox(rasterTile.rast.extent)
                rasterTile.save()
                rasterTile.groups.set(shapefileGroups)
                tilesLoaded += 1
            sys.stdout.flush()  # flush often because otherwise the ANSI escape sequence "cleverness" becomes clumsiness when it goes out of sync
    print("\t...loaded", str(tilesLoaded), "tiles and skipped", str(
        tilesSkipped), "because they contained only NODATA pixels.")
    # clear remaining detritus from GDAL_ERRORs
    print("                                                                                          ")
    sys.stdout.write("\033[F\033[K")


def run(verbose=True):

    ######################################################
    # GENERATED CODE GOES HERE
    # DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
    # loadGroups
    from disasterinfosite.models import ShapefileGroup
    wildfire_shapefilegroup, _ = ShapefileGroup.objects.get_or_create(name='wildfire')
    winter_shapefilegroup, _ = ShapefileGroup.objects.get_or_create(name='winter')
    summer_shapefilegroup, _ = ShapefileGroup.objects.get_or_create(name='summer')
    quake_shapefilegroup, _ = ShapefileGroup.objects.get_or_create(name='quake')
    flood_shapefilegroup, _ = ShapefileGroup.objects.get_or_create(name='flood')
    # END OF GENERATED CODE BLOCK
    ######################################################

    ######################################################
    # GENERATED CODE GOES HERE
    # DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
    # loadImports
    print('Loading data for Ravalli_co')
    from disasterinfosite.models import Ravalli_co
    lm_Ravalli_co = LayerMapping(Ravalli_co, Ravalli_co_shp, Ravalli_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Ravalli_co.save()
    for instance in Ravalli_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Silverbow_co')
    from disasterinfosite.models import Silverbow_co
    lm_Silverbow_co = LayerMapping(Silverbow_co, Silverbow_co_shp, Silverbow_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Silverbow_co.save()
    for instance in Silverbow_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for AllCounties')
    from disasterinfosite.models import AllCounties
    lm_AllCounties = LayerMapping(AllCounties, AllCounties_shp, AllCounties_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_AllCounties.save()
    for instance in AllCounties.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for fire_wui_wmt')
    from disasterinfosite.models import fire_wui_wmt
    lm_fire_wui_wmt = LayerMapping(fire_wui_wmt, fire_wui_wmt_shp, fire_wui_wmt_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_fire_wui_wmt.save()
    for instance in fire_wui_wmt.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
    print('Loading data for Burned_perimeter')
    from disasterinfosite.models import Burned_perimeter
    lm_Burned_perimeter = LayerMapping(Burned_perimeter, Burned_perimeter_shp, Burned_perimeter_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Burned_perimeter.save()
    for instance in Burned_perimeter.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
    print('Loading data for WHP_FINAL')
    from disasterinfosite.models import WHP_FINAL
    lm_WHP_FINAL = LayerMapping(WHP_FINAL, WHP_FINAL_shp, WHP_FINAL_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_WHP_FINAL.save()
    for instance in WHP_FINAL.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
    print('Loading data for DeerLodge_co')
    from disasterinfosite.models import DeerLodge_co
    lm_DeerLodge_co = LayerMapping(DeerLodge_co, DeerLodge_co_shp, DeerLodge_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_DeerLodge_co.save()
    for instance in DeerLodge_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Missoula_co')
    from disasterinfosite.models import Missoula_co
    lm_Missoula_co = LayerMapping(Missoula_co, Missoula_co_shp, Missoula_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Missoula_co.save()
    for instance in Missoula_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Granite_co')
    from disasterinfosite.models import Granite_co
    lm_Granite_co = LayerMapping(Granite_co, Granite_co_shp, Granite_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Granite_co.save()
    for instance in Granite_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Flathead_co')
    from disasterinfosite.models import Flathead_co
    lm_Flathead_co = LayerMapping(Flathead_co, Flathead_co_shp, Flathead_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flathead_co.save()
    for instance in Flathead_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Beaverhead_co')
    from disasterinfosite.models import Beaverhead_co
    lm_Beaverhead_co = LayerMapping(Beaverhead_co, Beaverhead_co_shp, Beaverhead_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Beaverhead_co.save()
    for instance in Beaverhead_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Gallatin_co')
    from disasterinfosite.models import Gallatin_co
    lm_Gallatin_co = LayerMapping(Gallatin_co, Gallatin_co_shp, Gallatin_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Gallatin_co.save()
    for instance in Gallatin_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Lincoln_co')
    from disasterinfosite.models import Lincoln_co
    lm_Lincoln_co = LayerMapping(Lincoln_co, Lincoln_co_shp, Lincoln_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Lincoln_co.save()
    for instance in Lincoln_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for MergedEQs')
    from disasterinfosite.models import MergedEQs
    lm_MergedEQs = LayerMapping(MergedEQs, MergedEQs_shp, MergedEQs_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_MergedEQs.save()
    for instance in MergedEQs.objects.all():
        instance.groups.add(quake_shapefilegroup)
    print('Loading data for Mineral_co')
    from disasterinfosite.models import Mineral_co
    lm_Mineral_co = LayerMapping(Mineral_co, Mineral_co_shp, Mineral_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Mineral_co.save()
    for instance in Mineral_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for FloodMaps_MT')
    from disasterinfosite.models import FloodMaps_MT
    lm_FloodMaps_MT = LayerMapping(FloodMaps_MT, FloodMaps_MT_shp, FloodMaps_MT_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_FloodMaps_MT.save()
    for instance in FloodMaps_MT.objects.all():
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Lake_co')
    from disasterinfosite.models import Lake_co
    lm_Lake_co = LayerMapping(Lake_co, Lake_co_shp, Lake_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Lake_co.save()
    for instance in Lake_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Sanders_co')
    from disasterinfosite.models import Sanders_co
    lm_Sanders_co = LayerMapping(Sanders_co, Sanders_co_shp, Sanders_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Sanders_co.save()
    for instance in Sanders_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for Madison_co')
    from disasterinfosite.models import Madison_co
    lm_Madison_co = LayerMapping(Madison_co, Madison_co_shp, Madison_co_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Madison_co.save()
    for instance in Madison_co.objects.all():
        instance.groups.add(wildfire_shapefilegroup)
        instance.groups.add(winter_shapefilegroup)
        instance.groups.add(summer_shapefilegroup)
        instance.groups.add(quake_shapefilegroup)
        instance.groups.add(flood_shapefilegroup)
    print('Loading data for CMZ_mt')
    from disasterinfosite.models import CMZ_mt
    lm_CMZ_mt = LayerMapping(CMZ_mt, CMZ_mt_shp, CMZ_mt_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_CMZ_mt.save()
    for instance in CMZ_mt.objects.all():
        instance.groups.add(flood_shapefilegroup)
    # END OF GENERATED CODE BLOCK
    ######################################################

    print("Data load finished.  GDAL_ERROR 'Failed to compute statistics, no valid pixels found in sampling' is safe to ignore if the data includes any raster files with any NODATA pixels.")


class Command(BaseCommand):
    help = """ Load data from the data directory """

    def handle(self, *args, **options):
        run()
