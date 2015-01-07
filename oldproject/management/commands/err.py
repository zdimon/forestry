# -*- coding: utf-8 -*-

import logging
logging.basicConfig()
from optparse import make_option

from django.utils.importlib import import_module

from django.core.management.base import BaseCommand, CommandError
from fires.models import Fires, Meteocondition, Fires2FireWorked, FireWorked, Fires2GeoPolygon, Fires2FireWorked
from forestry.models import GeoPolygon, Forestry
from clasterization.models import DecisionTable
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

  #      DecisionTable.objects.all().delete()


        for d in Forestry.objects.all():
            d.forestry_group_id = 1
            d.save()
