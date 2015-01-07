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
        from oldproject.models import Fires2ExtingCosts as Oldfires2ec
        from fires.models import Fires2ExtingCosts, Fires, ExtingCosts
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        Fires2ExtingCosts.objects.all().delete()
        for fg in Oldfires2ec.objects.all():
            print fg.id
                           #forestry = Forestry.objects.get(old_id=1)
            #try:
            exting_costs = ExtingCosts.objects.get(old_id=fg.exting_costs_id)
            print exting_costs.id
            fires = Fires.objects.get(old_id=fg.fire_id)
            #    logger.info(ss.id)
            g = Fires2ExtingCosts()
            g.exting_costs = exting_costs
            g.fire = fires
            g.sum = fg.sum
            #import pdb; pdb.set_trace()
            g.save()
            #except:
             #   pass
        logger.info("Finish transfering.....")
