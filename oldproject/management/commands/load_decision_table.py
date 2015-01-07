# -*- coding: utf-8 -*-

import logging
logging.basicConfig()
from optparse import make_option

from django.utils.importlib import import_module

from django.core.management.base import BaseCommand, CommandError
from fires.models import Fires, Meteocondition, Fires2FireWorked, FireWorked, Fires2GeoPolygon, Fires2FireWorked
from forestry.models import GeoPolygon
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


        for d in  DecisionTable.objects.all():
            fi = d.ground_square
            print fi




        for d in  DecisionTable.objects.all():
            fi = d.fire_id
            f = Fires.objects.get(id=fi)
            da = f.date_begin
            m = Meteocondition.objects.filter(curdate=da)
            if m.count()>0:
    #            print "Hi"
                p = m[0].pjc
     #           print(p)
                pr = m[0].pr
      #          print(pr)
            else:
                p = m.pjc
       #         print(p)
                pr = m.pr
        #        print(pr)
            d.pjc = p
            d.pr = pr
            d.save()


        for d in  DecisionTable.objects.all():
            fi = d.fire_id
            #f = Fires.objects.get(id=fi)
            f = Fires2GeoPolygon.objects.filter(fire_id=fi)
            if f:
                #f = Fires2GeoPolygon.objects.get(fire_id=fi)
                v = f[0].geo_polygon_id
                gp = GeoPolygon.objects.filter(id=v)
                if gp:
                    w = gp[0].wood_volume_per_ha
                    d.wood_volume_per_ha = w
                    print w
                else:
                    print 11


            else:
                print "error"
                fg = Fires.objects.get(id = fi)
                da = fg.date_begin
                print da
            d.save()



        for d in DecisionTable.objects.all():
            fi = d.fire_id
            fw = Fires2FireWorked.objects.filter(fire_id=fi)
            if fw.count()>0:
                print "ok"
                i = 0
                while i < fw.count():
                    if fw[i].fire_worked_id==1:
                        d.forestry_man_days = fw[i].num
                    if fw[i].fire_worked_id==2:
                        d.emergency_man_days = fw[i].num
                    if fw[i].fire_worked_id==3:
                        d.another_man_days = fw[i].num
                    if fw[i].fire_worked_id==4:
                        d.forestry_fire_eng = fw[i].num
                    if fw[i].fire_worked_id==5:
                        d.forestry_another = fw[i].num
                    if fw[i].fire_worked_id==6:
                        d.emergency_fire_eng = fw[i].num
                    if fw[i].fire_worked_id==7:
                        d.emergency_another = fw[i].num
                    if fw[i].fire_worked_id==8:
                        d.another_fire_eng = fw[i].num
                    if fw[i].fire_worked_id==9:
                        d.another_another = fw[i].num
                    if fw[i].fire_worked_id==10:
                        d.total_fire_eng = fw[i].num
                    if fw[i].fire_worked_id==11:
                        d.total_another = fw[i].num
                    i += 1

            else:
                print "Bye"
            d.save()



   #     for d in DecisionTable.objects.all():

  #          fi = d.fire_id
   #         f = Fires.objects.get(id=fi)
    #        b = f.exting_begin
#            e = f.exting_end
#            t = e - b
#            print t

 #       b = type(t)
  #      print b

            #d.save()



            #try:
             #   m = GeoPolygon.objects.filter(id=fgi)
              #  w = m[0:1].wood_volume_per_ha
#                if w:
#                    d.wood_volume_per_ha = w
#                else:
#                    d.wood_volume_per_ha = 0
#            except:
#                print "error"

#            d.save()