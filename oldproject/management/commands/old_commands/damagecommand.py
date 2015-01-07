from django.core.management.base import BaseCommand, CommandError
from map.models import Fires, GeoPolygon
from random import randint
from django.db.models import Avg, Max, Min

#class Command(BaseCommand):

 #   def handle(self, *args, **options):
  #      for g in GeoPolygon.objects.all().filter(type_id=1):
   #         r = randint(1,9)
    #        g.firerisk = r
     #       g.save()
      #      print (r)





class Command(BaseCommand):






    def handle(self, *args, **options):

        print "This is a command"
        geopolygons = GeoPolygon.objects.all()
        l = geopolygons.aggregate(m=Min('wood_volume_per_ha'))
        print (l)
        h = geopolygons.aggregate(ma = Max('wood_volume_per_ha'))
        print(h)

        a = int(l['m'])
        print(a)
        b = int(h['ma'])
        print(b)
        d = b - a
        print(d)

# The number of classes
        n = 4
        print(n)
# Value of interval
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





        for g in GeoPolygon.objects.all():
            r = 0
            g.class_damage = r
            g.save()
            print (r)
    #    w=0

        for g in GeoPolygon.objects.all():
            i = 0
            while i < n:
                i += 1
                if g.wood_volume_per_ha > aa[i-1] and g.wood_volume_per_ha <= aa[i]:
                    g.class_damage = i
             #   if g.wood_volume_per_ha > aa[n-1]:    
           #         g.class_damage = n
            #        w = w + 1
      
                    g.save()
                    print (i)

#        print(w)            
        z = aa[n-1]
        print z
        print n
        for g in GeoPolygon.objects.all():
            if g.wood_volume_per_ha > z:
                g.class_damage = n
                g.save()





        #for f in Fires.objects.all():

         #   self.stdout.write('Successfully closed poll "%s"' % f.id)
