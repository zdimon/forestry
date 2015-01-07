from django.core.management.base import BaseCommand, CommandError
from map.models import Fires, GeoPolygon
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
        for g in GeoPolygon.objects.all():
            q = g.wood_volume_per_ha/10
            print(q)
            g.firerisk = q
            g.save()


        geopolygons = GeoPolygon.objects.all()
        l = geopolygons.aggregate(m=Min('firerisk'))
        print(l)
        h = geopolygons.aggregate(ma=Max('firerisk'))
        print(h)

        a = int(l['m'])
        print(a)
        b = int(h['ma'])
        print(b)
        d = b - a
        print(d)

        
        #the number of classes
        n = 4

        print(n)

        h = d / n
        print(h)

        i = 0
        aa = []
        aa.append(0)

        while i < n:
            print i
            i += 1
            q = aa[i-1] + h
            aa.append(q)
            print(aa[i])





# fire danger


        pr  = 0.053
#fire risk for all regions

        for g in GeoPolygon.objects.all():
            zzz = Decimal(g.wood_volume_per_ha)
            prz = Decimal(pr)
#            qq = g.wood_volume_per_ha * pr
            qq =  zzz * prz
            print(qq)
            g.firerisk = qq
            g.save()


# risk class for all regions


        for g in GeoPolygon.objects.all():
            r = 0
            g.class_risk1 = r
            g.save()
            print(r)


        for g in GeoPolygon.objects.all():
            i = 0
            while i < n:
                i +=1
                if g.firerisk > aa[i-1] and g.firerisk <= aa[i]:
                    g.class_risk1 = i
                    g.save()
                    print(i)

        z = aa[n-1]
        print(z)
        print(n)

        for g in GeoPolygon.objects.all():
            if g.firerisk > z:
                g.class_risk1 = n
                g.save()

    



        
          
        

    











