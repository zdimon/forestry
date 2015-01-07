from django.core.management.base import BaseCommand, CommandError
from map.models import Fires, GeoPolygon
from random import randint

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
            r = 0
            g.wood_volume_per_ha = r
            g.save()
            print (r)





        for g in GeoPolygon.objects.all().filter(type_id=1):
            r = randint(100,300)
            g.wood_volume_per_ha = r
            g.save()
            print (r)



        for g in GeoPolygon.objects.all().filter(type_id=2):
            r = randint(50,100)
            g.wood_volume_per_ha = r
            g.save()
            print (r)



        for g in GeoPolygon.objects.all().filter(type_id=3):
            r = randint(50,75)
            g.wood_volume_per_ha = r
            g.save()
            print (r)



        for g in GeoPolygon.objects.all().filter(type_id=5):
            r = randint(10,30)
            g.wood_volume_per_ha = r
            g.save()
            print (r)















        #for f in Fires.objects.all():

         #   self.stdout.write('Successfully closed poll "%s"' % f.id)
