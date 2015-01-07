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
        from oldproject.models import FireDamage as Oldfiredamage
        from oldproject.models import FireDamageTranslation as Oldfiredamagetranslation
        from fires.models import FireDamage
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        FireDamage.objects.all().delete()
        for fg in Oldfiredamage.objects.all():
            o = FireDamage()
            o.old_id = fg.id
            for ot in Oldfiredamagetranslation.objects.filter(fire_damage=fg):
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
