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
        from oldproject.models import ForestryGroup as Oldforestrygroup, ForestryGroupTranslation as oldtrans
        from forestry.models import ForestryGroup
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        ForestryGroup.objects.all().delete()
        for f in Oldforestrygroup.objects.all():
            nf = ForestryGroup()
            for ft in oldtrans.objects.filter(forestry_group_id = f.pk):
                if ft.lang=='ru':
                    nf.name_ru = ft.name
                    nf.name = ft.name
                elif ft.lang=='en':
                    nf.name_en = ft.name
                elif ft.lang=='uk':
                    nf.name_uk = ft.name
                nf.save()
        logger.info("Finish transfering.....")

