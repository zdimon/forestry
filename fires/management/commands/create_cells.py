# -*- coding: utf-8 -*-

import logging
logging.basicConfig()
from optparse import make_option

from django.contrib.gis.geos import Polygon
from django.contrib.gis.geos import GEOSGeometry
from math import *

from django.utils.importlib import import_module

from django.core.management.base import BaseCommand, CommandError
#from fires.models import Fires2GeoPolygon, Fires
#from forestry.models import GeoPolygon, GeoKvartal, GeoCell

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

        from forestry.models import Forestry, GeoKvartal, GeoPolygon, GeoCell
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        GeoCell.objects.all().delete()
	# Coordinates of top left corner
	up_left_lon = 32.81636
	up_left_lat = 46.66443112741369
	# Coordinates of lower right corner
	down_right_lon = 33.00518768307956
	down_right_lat = 46.58096009387599
	width = down_right_lon - up_left_lon
	height = up_left_lat - down_right_lat
	print width
	print height
	#Discretization interval
	hx = 0.002   #horizontal step
	hy = (hx / 24) * 17    #vertical step

	
	
	cury = up_left_lat + hy

	
	while cury > down_right_lat:
	    print "----------------------"		
	    cury = cury - hy
	    curx = up_left_lon - hx
	    while curx < down_right_lon:
		gc = GeoCell()
	        curx = curx + hx
		print curx, cury
#create cell and save it in the table
		#cell = Polygon(((curx, cury), (curx + hx, cury), (curx + hx, cury - hy), (curx, cury - hy), (curx, cury)))
		cell = 'MULTIPOLYGON(((%s %s, %s %s, %s %s, %s %s, %s %s)))' % (curx, cury, curx + hx, cury, curx + hx, cury - hy, curx, cury - hy, curx, cury)
		gc.geom = cell
		gc.save()

	
		


	

