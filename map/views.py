#coding: UTF-8

from django.conf import settings
from django.shortcuts import render_to_response
from djgeojson.views import GeoJSONLayerView


#from qsstats import QuerySetStats
from django.db.models import Count
from django.db.models import Max
from django.db.models import Sum
from django.db.models import Variance
from datetime import date

from datetime import datetime

#from highcharts.views import HighChartsLineView




from djgeojson.serializers import Serializer as GeoJSONSerializer
from djgeojson.http import HttpJSONResponse





def mapregion(request):
    from forestry.models import TypePolygon
    types = TypePolygon.objects.all().filter(is_pub=True).order_by('fill_color')
    base_url = request.build_absolute_uri('/')[:-1]
    return render_to_response('map/regions.html', {"types":types, "base_url": base_url})

