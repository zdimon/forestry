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
        from oldproject.models import TypePolygon as Oldtypepolygon, TypePolygonTranslation as oldtrans
        from forestry.models import TypePolygon
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        TypePolygon.objects.all().delete()
        for f in Oldtypepolygon.objects.all():
            nf = TypePolygon()
            nf.old_id=f.pk
            nf.is_pub = f.is_pub
            nf.fill_color = f.fill_color
            nf.border_color = f.border_color
            for ft in oldtrans.objects.filter(type_polygon_id = f.pk):
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