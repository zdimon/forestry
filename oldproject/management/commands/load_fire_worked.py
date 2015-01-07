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
        from oldproject.models import FireWorked as Oldfireworked
        from oldproject.models import FireWorkedTranslation as Oldfireworkedtranslation
        from fires.models import FireWorked
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        FireWorked.objects.all().delete()
        for fg in Oldfireworked.objects.all():
            o = FireWorked()
            o.old_id = fg.id
            for ot in Oldfireworkedtranslation.objects.filter(fire_worked_id=fg.id):
                print 'qq1'
                if ot.lang=='ru':
                    o.name=ot.name
                    o.name_ru=ot.name
                if ot.lang=='en':
                    o.name_en = ot.name
                if ot.lang=='uk':
                    o.name_uk = ot.name
            o.save()
        logger.info("Finish transfering.....")
