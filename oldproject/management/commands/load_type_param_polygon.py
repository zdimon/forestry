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
        from oldproject.models import TypeParamPolygon as Oldtpp, TypeParamPolygonTranslation as oldtppt
        from forestry.models import TypeParamPolygon, TypePolygon, TypeValue
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        TypeParamPolygon.objects.all().delete()
        for f in Oldtpp.objects.all():
            print f.id
            type_polygon = TypePolygon.objects.get(old_id=f.type_reg_id)
            type_value = TypeValue.objects.get(old_id=f.type_value_id)
            nf = TypeParamPolygon()
            nf.old_id=f.pk
            nf.type_reg = type_polygon
            nf.value = f.value
            nf.type_value = type_value
            for ft in oldtppt.objects.filter(type_param_polygon_id = f.pk):
                if ft.lang=='ru':
                    nf.name_ru = ft.name
                    nf.name = ft.name
                elif ft.lang=='en':
                    nf.name_en = ft.name
                elif ft.lang=='uk':
                    nf.name_uk = ft.name
                #nf.save()
            nf.save()
        logger.info("Finish transfering.....")