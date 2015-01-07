# -*- coding: utf-8 -*-

import logging
import random
from django.db.models import Max




logging.basicConfig()
from optparse import make_option


from fires.models import Fires, Meteocondition, Fires2FireWorked, FireWorked, Fires2GeoPolygon, Fires2FireWorked
from forestry.models import GeoPolygon
from clasterization.models import DecisionTable, Contradiction






from django.core.management.base import BaseCommand
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):


    def handle(self, *args, **options):
        from django.utils import timezone
        from clasterization.models import DecisionTable, Contradiction
        logger.info("Start transfering.....")
        logger.info("Clear table.....")

        Contradiction.objects.all().delete()

        for d in  DecisionTable.objects.all():
            gs = d.ground_square_gen
            cs = d.crowning_square_gen
            us = d.unforest_square_gen
            w = d.wood_volume_per_ha_gen
            pjc = d.pjc_gen
            pr = d.pr_gen
            a = d.assessment_gen
            cd = Contradiction()
            dt = DecisionTable.objects.filter(ground_square_gen=gs, crowning_square_gen = cs, unforest_square_gen = us, wood_volume_per_ha_gen = w, pjc_gen = pjc, pr_gen = pr).exclude(assessment_gen = a)  
            c = dt.count()
#            print c
            if c > 0:
                i = 0
                while i < c:
                    cd.ground_square_gen = dt[i].ground_square_gen
                    cd.crowning_square_gen = dt[i].crowning_square_gen
                    cd.unforest_square_gen = dt[i].unforest_square_gen
                    cd.wood_volume_per_ha_gen = dt[i].wood_volume_per_ha_gen
                    cd.pjc_gen = dt[i].pjc_gen
                    cd.pr_gen = dt[i].pr_gen
                    cd.assessment_gen = dt[i].assessment_gen
                    i = i + 1
                    
          
                    try:
                        q = Contradiction.objects.get(ground_square_gen = gs, crowning_square_gen = cs, unforest_square_gen = us, wood_volume_per_ha_gen = w, pjc_gen = pjc, pr_gen = pr, assessment_gen = a)
                    except:
                #import pdb; pdb.set_trace()
                #pass
                       cd.save()
     #       for r in Contradiction.objects.distinct():
#                r.save()
