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

        from fires.models import Fires, Fires2GeoPolygon

        from forestry.models import Forestry, GeoKvartal, GeoPolygon
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        Fires2GeoPolygon.objects.all().delete()

        f = file('/home/marina/ff_ve/forestry/fires/management/commands/Fires1.txt', 'r')
        # iterate over the lines in the file
        for line in f:
          # split the line into a list of column values
            columns = line.split(';')
    # clean any whitespace off the items
            columns = [col.strip() for col in columns]

    # ensure the column has at least one value before printing
            if columns:
                k = columns[7] # kvartal
                v = columns[8] # vydel
                d = columns[1] # date
                fid = columns[6] # forestry id
                dd = d.split('.')
                #import pdb; pdb.set_trace()
                #print dd
                #try:
                date = dd[2] + '-' + dd[1] + '-' + dd[0]
                t = columns[4] # time of the end of extinguishing
                  #  print t
                tt = t.split(',')
                if len(tt)==1:
                    time = tt[0] + ':00:00'
                else:
                    time = tt[0] + ':' + tt[1] + ':00'
                #print time
                #except:
                 #   import pdb; pdb.set_trace()
                   #import pdb; pdb.set_trace()
                dt = date + ' ' + time
                #print dt
                fire = Fires.objects.filter(date_end = dt)
                if fire:
                    fi = fire[0].id
                    print "hh"

                  #  try:

                    fire[0].forestry_id = fid

                    print fid

                    ft = Fires2GeoPolygon()
                    ft.fire_id = fi
                    ft.kvartal = k
                    ft.vydel = v
                    ft.save()

                       # qqq = Fires()

                    fire[0].save()

               #     except:
                #        import pdb; pdb.set_trace()

                else:
                    print "---"
                #ft.save

        for d in Fires.objects.all():
            if d.forestry_id==11 and d.forestry_group_id==1:
                id = d.id
            #f = Fires.objects.get(id=fi)
                f = Fires2GeoPolygon.objects.filter(fire_id=id)
                if f:
                    k = f[0].kvartal
                    g = GeoKvartal.objects.filter(number=k)
                    i = g[0].id

                    gp = GeoPolygon.objects.filter(kvartal_id=i)
                    if gp:
                        idd = gp[0].id
                        print idd
                        f[0].geo_polygon_id = idd
                        f[0].save()
                    else:
                        print"fff"


                else:
                    print "ppp"

