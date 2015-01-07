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
        from oldproject.models import Fires2FireWorked as Oldfires2fw
        from fires.models import Fires2FireWorked, Fires, FireWorked
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        Fires2FireWorked.objects.all().delete()
        for fg in Oldfires2fw.objects.all():
            print fg.id
                           #forestry = Forestry.objects.get(old_id=1)
            #try:
            fire_worked = FireWorked.objects.get(old_id=fg.fire_worked_id)
            print fire_worked.id
            fires = Fires.objects.get(old_id=fg.fire_id)
            #    logger.info(ss.id)
            g = Fires2FireWorked()
            g.fire_worked = fire_worked
            g.fire = fires
            g.num = fg.num
            #import pdb; pdb.set_trace()
            g.save()
            #except:
             #   pass
        logger.info("Finish transfering.....")
