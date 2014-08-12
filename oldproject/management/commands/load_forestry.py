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
        from oldproject.models import Forestry as Oldforestry
        from forestry.models import Forestry
        logger.info("Start transfering.....")
        for f in Oldforestry.objects.all():
            nf = Forestry()
            nf.name_ru = 'ssss'
            nf.save()
        logger.info("Finish transfering.....")

