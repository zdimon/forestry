from django.core.management.base import BaseCommand, CommandError
from map.models import Fires, GeoPolygon, DecisionTable, Meteocondition, Fires2FireWorked, FireWorked
from random import randint
from django.db.models import Avg, Max, Min
from decimal import Decimal
from decimal import *

#class Command(BaseCommand):

 #   def handle(self, *args, **options):
  #      for g in GeoPolygon.objects.all().filter(type_id=1):
   #         r = randint(1,9)
    #        g.firerisk = r

     #       g.save()
      #      print (r)


class Command(BaseCommand):

    def handle(self, *args, **options):
 #       for g in Fires.objects.all():
  #          q = g.id
   #         cr = g.crowning_square
    #        gr = g.ground_square
     #       un = g.unforest_square
      #      d = DecisionTable()
#            d.fire_id = q
#            d.crowning_square = cr
#            d.ground_square = gr
#            d.unforest_square = un
#            d.save()

#        for d in  DecisionTable.objects.all():
#            fi = d.fire_id
#            f = Fires.objects.get(id=fi)
#            da = f.date_begin
#            m = Meteocondition.objects.filter(curdate=da)
#            if m.count()>0:
#                print "Hi"
#                p = m[0].pjc
#                print(p)
#                pr = m[0].pr
#                print(pr)
#            else:
#                p = m.pjc
#                print(p)
#                pr = m.pr
#                print(pr)
#            d.pjc = p
#            d.pr = pr
#            d.save()


        for d in DecisionTable.objects.all():
            fi = d.fire_id
            fw = Fires2FireWorked.objects.filter(fire_id=fi)
            if fw.count()>0:
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



































#            print da



#            print(q)
#            print(cr)
#            print(gr)



#            g.firerisk = q
#            g.save()


#        geopolygons = GeoPolygon.objects.all()
 #       l = geopolygons.aggregate(m=Min('firerisk'))
#        print(l)
#        h = geopolygons.aggregate(ma=Max('firerisk'))
#        print(h)

#        a = int(l['m'])
#        print(a)
#        b = int(h['ma'])
#        print(b)
#        d = b - a
#        print(d)

        
        #the number of classes
#        n = 4

 #       print(n)

  #      h = d / n
   #     print(h)

    #    i = 0
     #   aa = []
      #  aa.append(0)

#        while i < n:
 #           print i
  #          i += 1
   #         q = aa[i-1] + h
    #        aa.append(q)
     #       print(aa[i])





# fire danger


      #  pr =  0.1
#fire risk for all regions

       # for g in GeoPolygon.objects.all():
        #    zzz = Decimal(g.wood_volume_per_ha)
         #   prz = Decimal(pr)
##            qq = g.wood_volume_per_ha * pr
#            qq =  zzz * prz
#            print(qq)
#            g.firerisk = qq
#            g.save()


    



        
          
        

    











