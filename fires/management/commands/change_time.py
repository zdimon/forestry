# -*- coding: utf-8 -*-

import logging
logging.basicConfig()
from optparse import make_option

from django.utils.importlib import import_module

from django.core.management.base import BaseCommand, CommandError
from fires.models import Fires2GeoPolygon, Fires
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
        f = file('/home/marina/ff_ve/forestry/fires/management/commands/Fires.txt', 'r')
        # iterate over the lines in the file
        for line in f:
          # split the line into a list of column values
            columns = line.split(';')
    # clean any whitespace off the items
            columns = [col.strip() for col in columns]

    # ensure the column has at least one value before printing
            if columns:
                d = columns[1] # date
                dd = d.split('.')
                #import pdb; pdb.set_trace()
                #print dd
                #try:
                date = dd[2] + '-' + dd[1] + '-' + dd[0]


                t1 = columns[3] # time of the begin of extinguishing
                tt1 = t1.split(',')
                if len(tt1)==1:
                    time1 = tt1[0] + ':00:00'
                else:
                    time1 = tt1[0] + ':' + tt1[1] + ':00'
                dt1 = date + ' ' + time1 #date-time of the begin of extinguishing
                print 'begin  '+ dt1


                t2 = columns[4] # time of the end of extinguishing
                tt2 = t2.split(',')
                if len(tt2)==1:
                    time2 = tt2[0] + ':00:00'
                else:
                    time2 = tt2[0] + ':' + tt2[1] + ':00'
                dt2 = date + ' ' + time2 #date-time of the end of extinguishing
                print 'end  '+ dt2

                for f in Fires.objects.all():
                    d = f.date_end[0:9]

                #fire = Fires.objects.filter(date_end[0:9] = date)



