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
        from oldproject.models import ForestElement2GeoPolygon as Oldforestelement2gp
        from forestry.models import ForestElement2GeoPolygon, GeoPolygon, ForestElement
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        ForestElement2GeoPolygon.objects.all().delete()
        for fg in Oldforestelement2gp.objects.all():
            print fg.id
                           #forestry = Forestry.objects.get(old_id=1)
            try:
                geo_polygon = GeoPolygon.objects.get(old_id=fg.geo_polygon_id)
                print geo_polygon.id
                forest_element = ForestElement.objects.get(old_id=fg.forest_element_id)
                #    logger.info(ss.id)
                g = ForestElement2GeoPolygon()
                g.geo_polygon = geo_polygon
                g.forest_element = forest_element
                g.age = fg.age
                g.height = fg.height
                g.diameter = fg.diameter
                g.wood_store = fg.wood_store
                g.percent = fg.percent
                g.save()
            except:
                pass
        logger.info("Finish transfering.....")
