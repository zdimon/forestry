from django.core.management.base import BaseCommand, CommandError
from map.models import Fires, GeoPolygon, Meteocondition
from random import randint
from django.db.models import Avg, Max, Min, Count
from decimal import Decimal
from decimal import *
import datetime, qsstats

#class Command(BaseCommand):

 #   def handle(self, *args, **options):
  #      for g in GeoPolygon.objects.all().filter(type_id=1):
   #         r = randint(1,9)
    #        g.firerisk = r
     #       g.save()
      #      print (r)





class Command(BaseCommand):






    def handle(self, *args, **options):
#        for g in GeoPolygon.objects.all():
 #           q = g.wood_volume_per_ha/10
  #          print(q)
   #         g.firerisk = q
    #        g.save()


#        meteos = Meteocondition.objects.all()
        meteos = GeoPolygon.objects.all()


#        meteo = qsstats.QuerySetStats(meteos, 'pr')
        meteo = qsstats.QuerySetStats(meteos, 'firerisk')


        day1 = datetime.date(2012, 4, 1)
        day2 = datetime.date(2012, 4, 30)


 #       time_series = meteo.time_series(day2, day1)
        time_series = meteo.time_series(day2, day1)



  #    l = geopolygons.aggregate(m=Min('firerisk'))
#        print(l)
#        h = geopolygons.aggregate(ma=Max('firerisk'))
#        print(h)

 #       a = int(l['m'])i
#        print(a)
#        b = int(h['ma'])
#        print(b)
#        d = b - a
#        print(d)

        
        #the number of classes
#        n = 4

#        print(n)

 #       h = d / n
  #      print(h)

   #     i = 0
    #    aa = []
     #   aa.append(0)

#        while i < n:
#            print i
#            i += 1
#            q = aa[i-1] + h
#            aa.append(q)
#            print(aa[i])



        
          
        

    











