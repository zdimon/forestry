# -*- coding: utf-8 -*-

import logging
logging.basicConfig()
from optparse import make_option

from django.core.management.base import BaseCommand
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):


    def handle(self, *args, **options):
        from oldproject.models import GeoPolygon as Oldgeopolygon
        from oldproject.models import GeoKvartal as Oldgeokvartal
        from oldproject.models import Forestry as Oldforestry
        from oldproject.models import TypePolygon as Oldtypepolygon
        from forestry.models import GeoPolygon, GeoKvartal, Forestry, TypePolygon
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        GeoPolygon.objects.all().delete()
        for fg in Oldgeopolygon.objects.all():
            try:
                kvartal = GeoKvartal.objects.get(old_id = fg.kvartal)
            except:
                kvartal = GeoKvartal.objects.get(old_id = 3)
            try:
                forestry = Forestry.objects.get(old_id=1)
                type_polygon = TypePolygon.objects.get(old_id=fg.type_id)
            #    logger.info(ss.id)
                g = GeoPolygon()
                g.kvartal = kvartal
                g.forestry = forestry
                g.type = type_polygon
                g.geom = fg.geom
                g.name = fg.name
                g.area = fg.area
                g.perimetr = fg.perimetr
                g.full_date = fg.full_date
                g.is_geom = fg.is_geom
                g.vydel = fg.vydel
                g.center_zoom = fg.center_zoom
                g.center_lon = fg.center_lon
                g.center_lat = fg.center_lat
                g.fire_able = fg.fire_able
                g.wood_volume_per_ha = fg.wood_volume_per_ha
                g.class_damage = fg.class_damage
                g.firedanger = fg.firedanger
                g.influence_probabiliti = fg.influence_probabiliti
                g.firerisk = fg.firerisk
                g.class_risk = fg.class_risk
                g.class_risk1 = fg.class_risk1
                g.class_risk2 = fg.class_risk2
                g.save()
                print 'polygon created '+str(g.id)
            except Exception, err:
                print Exception, err
                #import pdb; pdb.set_trace()




            #try:
            #    f = Forestry.objects.get(old_id = fg.forestry)
            #    logger.info(f.id)
            #except:
             #   pass
            #    import pdb; pdb.set_trace()






            #nf = Forestry()
            #nf.name_ru = 'ssss'
            #nf.save()
        #logger.info("Finish transfering.....")
