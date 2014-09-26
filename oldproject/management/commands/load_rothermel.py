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
        from oldproject.models import Rothermel as Oldrothermel, RothermelTranslation as oldtrans
        from fires.models import Rothermel
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        Rothermel.objects.all().delete()
        nf = Rothermel()
        nf.veget_type_id = 1
        nf.veget_type = 'aa'
        nf.veget_type_en = 'aa'
        nf.veget_type_ru = 'aa'
        nf.veget_type_uk = 'aa'
        nf.reserve = 12.1
        nf.unit_area = 11.2

        nf.save()
        logger.info("Finish transfering.....")