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
        from oldproject.models import ForestElement as Oldforestelement
        from oldproject.models import Rothermel as Oldrothermel
        from oldproject.models import TypePolygon as Oldtypepolygon
        from forestry.models import ForestElement, Rothermel, TypePolygon
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        ForestElement.objects.all().delete()
        for fg in Oldforestelement.objects.all():
            try:
                #forestry = Forestry.objects.get(old_id=1)
                type_polygon = TypePolygon.objects.get(old_id=fg.type_polygon_id)
            #    logger.info(ss.id)
                g = ForestElement()
                g.code = code
                g.rothermel_id = 1
                g.type_polygon = type_polygon
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
