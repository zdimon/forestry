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
        from oldproject.models import Forestry as Oldforestry, ForestryTranslation as ftr, ForestryGroup as Oldforestrygroup, ForestryGroupTranslation as oldtrans
        from forestry.models import Forestry, ForestryGroup
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        Forestry.objects.all().delete()
        for fg in ForestryGroup.objects.all():
            for oldf in Oldforestry.objects.filter(forestry_group_id = fg.old_id):
                logger.info(oldf.id)
                o = Forestry()
                o.old_id = oldf.id
                o.forestry_group = fg
                for ot in ftr.objects.filter(forestry_id=oldf.id):
                    if ot.lang=='ru':
                        o.name=ot.name
                        o.name_ru=ot.name
                    if ot.lang=='en':
                        o.name_en = ot.name
                    if ot.lang=='uk':
                        o.name_uk = ot.name
                o.save()
            #nf = Forestry()
            #nf.name_ru = 'ssss'
            #nf.save()
        #logger.info("Finish transfering.....")

