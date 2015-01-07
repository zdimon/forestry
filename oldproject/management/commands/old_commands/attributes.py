from django.core.management.base import BaseCommand, CommandError
from map.models import Fires, GeoPolygon, DecisionTable, Meteocondition, Fires2FireWorked, FireWorked, Fires2GeoPolygon
from random import randint
from django.db.models import Avg, Max, Min
from decimal import Decimal
from decimal import *



class Command(BaseCommand):

    def handle(self, *args, **options):

        for d in  DecisionTable.objects.all():
            fi = d.fire_id
            f = Fires2GeoPolygon.objects.filter(fire_id=fi)
            if f.count() >= 1:
                k = f[0].kvartal
                v = f[0].vydel
            g = GeoPolygon.objects.filter(kvartal=k, vydel=v)
            if g.count() > 0:
            #    print "Hi"
                w = g[0].wood_volume_per_ha
                d.wood_volume_per_ha = w;
                d.save()

     






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


    



        
          
        

    











