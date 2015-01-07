# -*- coding: utf-8 -*-

import logging
import random




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

  #      DecisionTable.objects.all().delete()
#        for fg in Oldfires.objects.all():
#            db = fg.date_begin
#            de = fg.date_end
#            eb = fg.exting_begin
#            ee = fg.exting_end
#            try:
#                fire_cause = FireCause.objects.get(old_id = fg.fire_cause)
#            except:
#                fire_cause = FireCause.objects.get(old_id = 3)
            #try:
#            forestry = Forestry.objects.get(old_id=1)
#            fire_detection = FireDetection.objects.get(old_id=fg.fire_detection_id)
        #    logger.info(ss.id)


#            g = DecisionTable()
#            g.fire_cause = fire_cause
#            g.forestry = forestry
#            g.fire_detection = fire_detection
#            g.date_begin = db
#            g.date_end = de
#            g.exting_begin = eb
#            g.exting_end = ee
#            g.square = fg.square
#            g.crowning_square = fg.crowning_square
#            g.ground_square = fg.ground_square
#            g.unforest_square = fg.unforest_square
#            g.date_month = fg.date_month
#            g.old_id = fg.id
#            g.save()


#        for d in  DecisionTable.objects.all():
#            da = d.date_begin
#            m = Meteocondition.objects.filter(curdate=da)
#            if m.count()>0:
    #            print "Hi"
#                p = m[0].pjc
     #           print(p)
#                pr = m[0].pr
      #          print(pr)
#            else:
#                p = m.pjc
       #         print(p)
#                pr = m.pr
        #        print(pr)
#            d.pjc = p
#            d.pr = pr
#            d.save()





        for d in  DecisionTable.objects.all():
            fi = d.fires_ptr

            f = Fires2GeoPolygon.objects.filter(fire_id=fi)
            if f:

                v = f[0].geo_polygon_id
                gp = GeoPolygon.objects.filter(id=v)
                if gp:
                    w = gp[0].wood_volume_per_ha
                    d.wood_volume_per_ha = w
                    #print w
                else:
                    aa = random.randint(160,200)
                    d.wood_volume_per_ha = aa
                    d.save()
     #               print aa


            else:
                d.wood_volume_per_ha = aa
      #          print "error"
                d.save()




        for d in DecisionTable.objects.all():
            fi = d.fires_ptr_id
            fw = Fires2FireWorked.objects.filter(fire_id=fi)
            if fw.count()>0:
                print "ok"
                i = 0
                while i < fw.count():
                    if fw[i].fire_worked_id==34:
                        d.forestry_man_days = fw[i].num
                        print "1"
                    if fw[i].fire_worked_id==35:
                        d.emergency_man_days = fw[i].num
                        print "2"
                    if fw[i].fire_worked_id==36:
                        d.another_man_days = fw[i].num
                        print "3"
                    if fw[i].fire_worked_id==37:
                        d.forestry_fire_eng = fw[i].num
                        print "4"
                    if fw[i].fire_worked_id==38:
                        d.forestry_another = fw[i].num
                        print "5"
                    if fw[i].fire_worked_id==39:
                        d.emergency_fire_eng = fw[i].num
                        print "6"
                    if fw[i].fire_worked_id==40:
                        d.emergency_another = fw[i].num
                        print "7"
                    if fw[i].fire_worked_id==41:
                        d.another_fire_eng = fw[i].num
                        print "8"
                    if fw[i].fire_worked_id==42:
                        d.another_another = fw[i].num
                        print "9"
                    if fw[i].fire_worked_id==43:
                        d.total_fire_eng = fw[i].num
                        print "10"
                    if fw[i].fire_worked_id==44:
                        d.total_another = fw[i].num
                        print "11"
                    d.save()
                    i += 1

            else:
                print "Bye"
            #d.save()



