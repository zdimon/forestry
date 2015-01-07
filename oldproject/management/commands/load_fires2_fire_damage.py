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
        from oldproject.models import Fires2FireDamage as Oldfires2fd
        from fires.models import Fires2FireDamage, Fires, FireDamage
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        Fires2FireDamage.objects.all().delete()
        for fg in Oldfires2fd.objects.all():
            print fg.id
                           #forestry = Forestry.objects.get(old_id=1)
            #try:
            fire_damage = FireDamage.objects.get(old_id=fg.fire_damage_id)
            print fire_damage.id
            fires = Fires.objects.get(old_id=fg.fire_id)
            #    logger.info(ss.id)
            g = Fires2FireDamage()
            g.fire_damage = fire_damage
            g.fire = fires
            g.sum = fg.sum
            #import pdb; pdb.set_trace()
            g.save()
            #except:
             #   pass
        logger.info("Finish transfering.....")
