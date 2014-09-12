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
                ss = GeoKvartal.objects.get(old_id = fg.kvartal)
            #    logger.info(ss.id)
            except:
                pass
                #import pdb; pdb.set_trace()

            try:
                f = Forestry.objects.get(old_id = fg.forestry)
                logger.info(f.id)
            except:
             #   pass
                import pdb; pdb.set_trace()






            #nf = Forestry()
            #nf.name_ru = 'ssss'
            #nf.save()
        #logger.info("Finish transfering.....")
