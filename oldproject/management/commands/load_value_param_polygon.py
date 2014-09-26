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
    ''' перенос лесничеств со старой базы в новую
    '''

    def handle(self, *args, **options):
        from oldproject.models import ValueParamPolygon as Oldvpp
        from forestry.models import ValueParamPolygon, TypePolygon, TypeParamPolygon, GeoPolygon
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        ValueParamPolygon.objects.all().delete()
        for f in Oldvpp.objects.all():
            print f.id
            type_polygon = TypePolygon.objects.get(old_id=f.type_reg_id)
            type_param_polygon = TypeParamPolygon.objects.get(old_id=f.type_param_id)
            polygon = GeoPolygon.objects.get(old_id=f.region_id)
            nf = ValueParamPolygon()
            nf.type_reg = type_polygon
            nf.value = f.value
            nf.region = polygon
            nf.type_param = type_param_polygon
            nf.save()
        logger.info("Finish transfering.....")