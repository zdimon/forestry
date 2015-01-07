# -*- coding: utf-8 -*-

import logging
import random
from django.db.models import Max




logging.basicConfig()
from optparse import make_option


from fires.models import Fires, Meteocondition, Fires2FireWorked, FireWorked, Fires2GeoPolygon, Fires2FireWorked
from forestry.models import GeoPolygon






from django.core.management.base import BaseCommand
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):


    def handle(self, *args, **options):
        from django.utils import timezone
        from oldproject.models import Fires as Oldfires
        from oldproject.models import FireCause as Oldfirecause
        from oldproject.models import Forestry as Oldforestry
        from oldproject.models import FireDetection as Oldfiredetection
        from fires.models import Fires, FireCause, FireDetection
        from clasterization.models import DecisionTable
        from forestry.models import Forestry
        logger.info("Start transfering.....")
        logger.info("Clear table.....")

        ground_square_max = DecisionTable.objects.all().aggregate(Max('ground_square')).values()[0]
        ground_square_delta = ground_square_max / 4
     #   print "ground_square_max" + str(ground_square_delta)
        crowning_square_max = DecisionTable.objects.all().aggregate(Max('crowning_square')).values()[0]
        crowning_square_delta = crowning_square_max / 4
#        print "crowning_square_max" + str(crowning_square_delta)
        unforest_square_max = DecisionTable.objects.all().aggregate(Max('unforest_square')).values()[0]
        unforest_square_delta = unforest_square_max / 4
#        print "unforest_square_max" + str(unforest_square_delta)
        wood_volume_per_ha_max = DecisionTable.objects.all().aggregate(Max('wood_volume_per_ha')).values()[0]
        wood_volume_per_ha_delta = wood_volume_per_ha_max / 4
#        print "wood_volume_per_ha_max" + str(wood_volume_per_ha_delta)
        pjc_max = DecisionTable.objects.all().aggregate(Max('pjc')).values()[0]
        pjc_delta = pjc_max / 4
#        print "pjc_max" + str(pjc_delta)
        pr_max = DecisionTable.objects.all().aggregate(Max('pr')).values()[0]
        pr_delta = pr_max / 4
#        print "pr_max" + str(pr_delta)


        for d in  DecisionTable.objects.all():
            if d.ground_square > 0 and d.ground_square <= ground_square_delta:
                d.ground_square_gen = "small"
            if d.ground_square > ground_square_delta and d.ground_square <= ground_square_delta*2:
                d.ground_square_gen = "average"
            if d.ground_square > ground_square_delta*2 and d.ground_square <= ground_square_delta*3:
                d.ground_square_gen = "big"
            if d.ground_square > ground_square_delta*3:
                d.ground_square_gen = "very big"

            if d.crowning_square > 0 and d.crowning_square <= crowning_square_delta:
                d.crowning_square_gen = "small"
            if d.crowning_square > crowning_square_delta and d.crowning_square <= crowning_square_delta*2:
                d.crowning_square_gen = "average"
            if d.crowning_square > crowning_square_delta*2 and d.crowning_square <= crowning_square_delta*3:
                d.crowning_square_gen = "big"
            if d.crowning_square > crowning_square_delta*3:
                d.crowning_square_gen = "very big"

            if d.unforest_square > 0 and d.unforest_square <= unforest_square_delta:
                d.unforest_square_gen = "small"
            if d.unforest_square > unforest_square_delta and d.unforest_square <= unforest_square_delta*2:
                d.unforest_square_gen = "average"
            if d.unforest_square > unforest_square_delta*2 and d.unforest_square <= unforest_square_delta*3:
                d.unforest_square_gen = "big"
            if d.unforest_square > unforest_square_delta*3:
                d.unforest_square_gen = "very big"

            if d.wood_volume_per_ha > 0 and d.wood_volume_per_ha <= wood_volume_per_ha_delta:
                d.wood_volume_per_ha_gen = "small"
            if d.wood_volume_per_ha > wood_volume_per_ha_delta and d.wood_volume_per_ha <= wood_volume_per_ha_delta*2:
                d.wood_volume_per_ha_gen = "average"
            if d.wood_volume_per_ha > wood_volume_per_ha_delta*2 and d.wood_volume_per_ha <= wood_volume_per_ha_delta*3:
                d.wood_volume_per_ha_gen = "big"
            if d.wood_volume_per_ha > wood_volume_per_ha_delta*3:
                d.wood_volume_per_ha_gen = "very big"

            if d.pjc > 0 and d.pjc <= pjc_delta:
                d.pjc_gen = "low"
            if d.pjc > pjc_delta and d.pjc <= pjc_delta*2:
                d.pjc_gen = "average"
            if d.pjc > pjc_delta*2 and d.pjc <= pjc_delta*3:
                d.pjc_gen = "high"
            if d.pjc > pjc_delta*3:
                d.pjc_gen = "critical"

            if d.pr > 0 and d.pr <= pr_delta:
                d.pr_gen = "low"
            if d.pr > pr_delta and d.pr <= pr_delta*2:
                d.pr_gen = "average"
            if d.pr > pr_delta*2 and d.pr <= pr_delta*3:
                d.pr_gen = "high"
            if d.pr > pr_delta*3:
                d.pr_gen = "critical"

            if d.forestry_man_days > 0 and d.forestry_fire_eng > 0 and d.emergency_another==0 and d.emergency_man_days==0 and d.emergency_fire_eng==0 and d.forestry_another==0 and d.another_man_days==0 and d.another_fire_eng==0 and d.another_another==0:
                d.assessment_gen = "low"
            if d.forestry_man_days > 0 and d.forestry_fire_eng > 0 and d.emergency_another>0 and d.emergency_man_days==0 and d.emergency_fire_eng==0 and d.forestry_another==0 and d.another_man_days==0 and d.another_fire_eng==0 and d.another_another==0:
                d.assessment_gen = "average"
            if d.emergency_another>0 or d.emergency_man_days>0 or d.emergency_fire_eng > 0:
                d.assessment_gen = "high"
            if d.another_man_days > 0 or d.another_fire_eng > 0 or d.another_another > 0:
                d.assessment_gen = "critical"
#            if d.assessment > assessment_delta*3:
#                d.assessment_gen = "critical"

            d.save()