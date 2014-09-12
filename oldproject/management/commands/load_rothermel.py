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
        for f in Oldrothermel.objects.all():
            nf = Rothermel()
            nf.old_id=f.pk
            for ft in oldtrans.objects.filter(rothermel_id = f.pk):
                if ft.lang=='ru':
                    nf.veget_type_ru = ft.veget_type
                    nf.veget_type = ft.veget_type
                elif ft.lang=='en':
                    nf.veget_type_en = ft.veget_type
                elif ft.lang=='uk':
                    nf.veget_type_uk = ft.veget_type
                nf.save()
        logger.info("Finish transfering.....")