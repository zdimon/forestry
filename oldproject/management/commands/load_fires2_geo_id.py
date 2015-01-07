# -*- coding: utf-8 -*-

import logging
logging.basicConfig()
from optparse import make_option

from django.utils.importlib import import_module

from django.core.management.base import BaseCommand, CommandError
from fires.models import Fires2GeoPolygon
from forestry.models import GeoPolygon, GeoKvartal

from random import randint
from django.db.models import Avg, Max, Min
from decimal import Decimal
from decimal import *


from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):


    def handle(self, *args, **options):
        for gg in Fires2GeoPolygon.objects.all():
            k = gg.kvartal
            v = gg.vydel
            g = GeoKvartal.objects.filter(number=k)
            if g:
                ki = g[0].id            # block identifier
                #print ki
                gp = GeoPolygon.objects.filter(kvartal_id=ki, vydel = v)
                if gp:
                    print "good"
                    gi = gp[0].id
                    gg.geo_polygon_id = gi

                else:
                    print "null"
            else:
                print "111"
            gg.save()

