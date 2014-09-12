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
        from oldproject.models import GeoKvartal as Oldgeokvartal, ForestryTranslation as ftr, Forestry as Oldforestry, ForestryGroupTranslation as oldtrans
        from forestry.models import Forestry, GeoKvartal
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        GeoKvartal.objects.all().delete()
        for fg in Forestry.objects.all():
            for oldf in Oldgeokvartal.objects.filter(forestry_id = fg.old_id):
                logger.info(oldf.id)
                o = GeoKvartal()
                o.forestry = fg
                o.oid=oldf.oid
                o.number=oldf.number
                o.area=oldf.area
                o.area_count = oldf.area_count
                o.perimetr = oldf.perimetr
                o.center_zoom = oldf.center_zoom
                o.center_lon = oldf.center_lon
                o.center_lat = oldf.center_lat
                o.geom = oldf.geom
                o.old_id=oldf.id
                o.save()
            #nf = Forestry()
            #nf.name_ru = 'ssss'
            #nf.save()
        #logger.info("Finish transfering.....")
