import os
from django.contrib.gis.utils import LayerMapping


######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadMappings
EQ_Fault_Buffer_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_Fault_Shaking_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_Fault_Worst_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

EQ_Historic_Distance_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Fire_Burn_Probability2_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Fire_Hist_Bound2_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Fire_Worst_Case_ph2_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_Channel_Migration_Zones_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_FEMA_DFRIM_2015_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Flood_Worst_Case_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

Landslide_placeholder2_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

summerstorm_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}

winterstorm_mapping = {
    'lookup_val': 'lookup_val',
    'geom': 'MULTIPOLYGON'
}


EQ_Fault_Buffer_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_Fault_Buffer.shp'))
EQ_Fault_Shaking_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_Fault_Shaking.shp'))
EQ_Fault_Worst_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_Fault_Worst.shp'))
EQ_Historic_Distance_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/EQ_Historic_Distance.shp'))
Fire_Burn_Probability2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Fire_Burn_Probability2.shp'))
Fire_Hist_Bound2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Fire_Hist_Bound2.shp'))
Fire_Worst_Case_ph2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Fire_Worst_Case_ph2.shp'))
Flood_Channel_Migration_Zones_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_Channel_Migration_Zones.shp'))
Flood_FEMA_DFRIM_2015_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_FEMA_DFRIM_2015.shp'))
Flood_Worst_Case_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Flood_Worst_Case.shp'))
Landslide_placeholder2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/Landslide_placeholder2.shp'))
summerstorm_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/summerstorm.shp'))
winterstorm_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../disasterinfosite/data/simplified/winterstorm.shp'))
# END OF GENERATED CODE BLOCK
######################################################


def run(verbose=True):

######################################################
# GENERATED CODE GOES HERE
# DO NOT MANUALLY EDIT CODE IN THIS SECTION - IT WILL BE OVERWRITTEN
# loadImports
    from .models import EQ_Fault_Buffer
    lm_EQ_Fault_Buffer = LayerMapping(EQ_Fault_Buffer, EQ_Fault_Buffer_shp, EQ_Fault_Buffer_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_Fault_Buffer.save(strict=True, verbose=verbose)

    from .models import EQ_Fault_Shaking
    lm_EQ_Fault_Shaking = LayerMapping(EQ_Fault_Shaking, EQ_Fault_Shaking_shp, EQ_Fault_Shaking_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_Fault_Shaking.save(strict=True, verbose=verbose)

    from .models import EQ_Fault_Worst
    lm_EQ_Fault_Worst = LayerMapping(EQ_Fault_Worst, EQ_Fault_Worst_shp, EQ_Fault_Worst_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_Fault_Worst.save(strict=True, verbose=verbose)

    from .models import EQ_Historic_Distance
    lm_EQ_Historic_Distance = LayerMapping(EQ_Historic_Distance, EQ_Historic_Distance_shp, EQ_Historic_Distance_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_EQ_Historic_Distance.save(strict=True, verbose=verbose)

    from .models import Fire_Burn_Probability2
    lm_Fire_Burn_Probability2 = LayerMapping(Fire_Burn_Probability2, Fire_Burn_Probability2_shp, Fire_Burn_Probability2_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Fire_Burn_Probability2.save(strict=True, verbose=verbose)

    from .models import Fire_Hist_Bound2
    lm_Fire_Hist_Bound2 = LayerMapping(Fire_Hist_Bound2, Fire_Hist_Bound2_shp, Fire_Hist_Bound2_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Fire_Hist_Bound2.save(strict=True, verbose=verbose)

    from .models import Fire_Worst_Case_ph2
    lm_Fire_Worst_Case_ph2 = LayerMapping(Fire_Worst_Case_ph2, Fire_Worst_Case_ph2_shp, Fire_Worst_Case_ph2_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Fire_Worst_Case_ph2.save(strict=True, verbose=verbose)

    from .models import Flood_Channel_Migration_Zones
    lm_Flood_Channel_Migration_Zones = LayerMapping(Flood_Channel_Migration_Zones, Flood_Channel_Migration_Zones_shp, Flood_Channel_Migration_Zones_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_Channel_Migration_Zones.save(strict=True, verbose=verbose)

    from .models import Flood_FEMA_DFRIM_2015
    lm_Flood_FEMA_DFRIM_2015 = LayerMapping(Flood_FEMA_DFRIM_2015, Flood_FEMA_DFRIM_2015_shp, Flood_FEMA_DFRIM_2015_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_FEMA_DFRIM_2015.save(strict=True, verbose=verbose)

    from .models import Flood_Worst_Case
    lm_Flood_Worst_Case = LayerMapping(Flood_Worst_Case, Flood_Worst_Case_shp, Flood_Worst_Case_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Flood_Worst_Case.save(strict=True, verbose=verbose)

    from .models import Landslide_placeholder2
    lm_Landslide_placeholder2 = LayerMapping(Landslide_placeholder2, Landslide_placeholder2_shp, Landslide_placeholder2_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_Landslide_placeholder2.save(strict=True, verbose=verbose)

    from .models import summerstorm
    lm_summerstorm = LayerMapping(summerstorm, summerstorm_shp, summerstorm_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_summerstorm.save(strict=True, verbose=verbose)

    from .models import winterstorm
    lm_winterstorm = LayerMapping(winterstorm, winterstorm_shp, winterstorm_mapping, transform=True, encoding='UTF-8', unique=['lookup_val'])
    lm_winterstorm.save(strict=True, verbose=verbose)

# END OF GENERATED CODE BLOCK
######################################################

