from django.contrib import admin
from forestry.models import ForestryGroup, Forestry, TypePolygon, GeoKvartal, GeoPolygon, ForestElement, ForestElement2GeoPolygon, TypeValue, TypeParamPolygon, ParamValueSelect, ValueParamPolygon
from fires.models import Rothermel
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline

from modeltranslation.admin import TranslationAdmin
from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from django.conf import settings
from django.template import RequestContext

from django.conf.urls import patterns, url
from django.http import HttpResponse

import django_databrowse
django_databrowse.site.register(GeoKvartal)

USE_GOOGLE_TERRAIN_TILES = False

from django.shortcuts import render_to_response
from djgeojson.views import GeoJSONLayerView
from map.views import  mapregion
from django.conf import settings
from djgeojson.serializers import Serializer as GeoJSONSerializer

class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization




class GetPolygonJsonFirerisk(GeoJSONLayerView):
    # Options
    from config.settings import BASE_DIR
    precision = 4   # float
    simplify = 0.5  # generalization
    def get_queryset(self):
        return GeoPolygon.objects.all()

    def render_to_response(self, context, **response_kwargs):
        from config.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/firerisk.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response





class GetPolygonJson(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization
    def get_queryset(self):
        if(self.request.GET['id']=='0'):
            return GeoPolygon.objects.all()
        else:
            return GeoPolygon.objects.all().filter(type_id=int(self.request.GET['id']))

    def render_to_response(self, context, **response_kwargs):
        from config.settings import BASE_DIR
        import os.path
        cpath = BASE_DIR+'/map_cache/'+self.request.GET['id']+'.txt'
        if(os.path.exists(cpath)):
            from django.http import HttpResponse
            f = open(cpath,'r')
            out = f.read()
            f.close()
            return HttpResponse(out, content_type="application/json")

        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        options = dict(properties=self.properties,
                       precision=self.precision,
                       simplify=self.simplify,
                       srid=self.srid,
                       geometry_field=self.geometry_field,
                       force2d=self.force2d)
        serializer.serialize(self.get_queryset(), stream=response, ensure_ascii=False,
                             **options)

        #import pdb; pdb.set_trace()
        f = open(cpath,'w')
        f.write(response.content)
        f.close()
        return response

# Kvartals
def sections(request): 
    base_url = request.build_absolute_uri('/')[:-1]
    return render_to_response('map/sections.html', {'user': request.user, 'base_url': base_url})

# Vydels
def regions(request):
    from forestry.models import TypePolygon
    types = TypePolygon.objects.all().filter(is_pub=True).order_by('fill_color')
    base_url = request.build_absolute_uri('/')[:-1]
    return render_to_response('map/regions.html', {"types":types, 'user': request.user, 'base_url': base_url})

#    
#    
#    base_url = request.build_absolute_uri('/')[:-1]
#    return render_to_response('map/regions.html', { "base_url": base_url})


# Fire risk
def risk(request,risk):
    base_url = request.build_absolute_uri('/')[:-1]
    legend = [['0', '#90EE90'],
          ['0-66', '#FFAEB9'],
          ['66-132', '#FA8072'],
          ['132 - 198', '#FF4040'],
          ['> 198', '#FF0000']]
    context = {'base_url': base_url, 'risk': risk, 'legend': legend}
    return render_to_response('map/risk.html', context, RequestContext(request))



    
def get_kvartal_info(request):    
    pass

def get_region_info(request):    
    region_id = request.GET['id']
    region = GeoPolygon.objects.all().get(pk=region_id)
    base_url = request.build_absolute_uri('/')[:-1]
    fe = ForestElement2GeoPolygon.objects.all().filter(geo_polygon=region_id)
    return render_to_response('map/region_info.html', {"region_id": region_id, "region": region, "fe": fe, "base_url": base_url })
    
def get_kvartal(request):    
    pass    
    
  

class ForestryAdmin(TranslationAdmin):
    pass
    
admin.site.register(Forestry, ForestryAdmin)


class ForestryInline(TranslationTabularInline):
    model = Forestry

class ForestryGroupAdmin(TranslationAdmin):
    list_display = ('name',)
    inlines = [ForestryInline,]
    fieldsets = [
        (u'ForestryGroups', {'fields': ('name',)})
    ]
admin.site.register(ForestryGroup, ForestryGroupAdmin)

class GeoKvartalAdmin(OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]


admin.site.register(GeoKvartal, GeoKvartalAdmin)


class TypePolygonAdmin(TranslationAdmin):
    list_display = ['__unicode__', 'fill_color', 'border_color', 'fill_color_rect', 'border_color_rect', 'is_pub']
    list_editable = ['is_pub', 'fill_color', 'border_color']
admin.site.register(TypePolygon, TypePolygonAdmin)


class GeoPolygonAdmin(OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = ['http://openstreetmap.org/openlayers/OpenStreetMap.js', 'http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s' % settings.GOOGLE_MAPS_API_KEY]
    list_display = ['__unicode__', 'wood_volume_per_ha']
    search_fields = ['=kvartal', '=vydel']
    list_editable = ['wood_volume_per_ha']
admin.site.register(GeoPolygon, GeoPolygonAdmin)


class ForestElement2GeoPolygonAdmin(admin.ModelAdmin):
    list_display = ('geo_polygon', 'forest_element', 'age', 'height', 'diameter', 'wood_store', 'percent',)
    fieldsets = [
        (u'ForestElement2GeoPolygons', {'fields': ('geo_polygon', 'forest_element', 'age', 'height', 'diameter', 'wood_store', 'percent',)})
    ]
admin.site.register(ForestElement2GeoPolygon, ForestElement2GeoPolygonAdmin)


class ForestElementAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'ForestElements', {'fields': ('name',)})
    ]
admin.site.register(ForestElement, ForestElementAdmin)


class TypeValueAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'TypeValues', {'fields': ('name',)})
    ]
admin.site.register(TypeValue, TypeValueAdmin)


class TypeParamPolygonAdmin(TranslationAdmin):
    list_display = ('type_reg', 'type_value', 'name', 'value',)
    fieldsets = [
        (u'TypeParamPolygons', {'fields': ('type_reg', 'type_value', 'name', 'value',)})
    ]
admin.site.register(TypeParamPolygon, TypeParamPolygonAdmin)


class ParamValueSelectAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (u'ParamValueSelects', {'fields': ('name',)})
    ]
admin.site.register(ParamValueSelect, ParamValueSelectAdmin)


class ValueParamPolygonAdmin(admin.ModelAdmin):
    list_display = ('type_reg', 'region', 'type_param', 'value',)
    fieldsets = [
        (u'TypeValues', {'fields': ('type_reg', 'region', 'type_param', 'value',)})
    ]

    def get_urls(self):
        urls = super(ValueParamPolygonAdmin, self).get_urls()

        my_urls = patterns('',
            url(r'^sections/$', admin.site.admin_view(sections)),
            url(r'^regions/$', admin.site.admin_view(regions)),
            url(r'^risk/(?P<risk>\w+)$', admin.site.admin_view(risk)),
            url(r'^get-kvartal-info/$', admin.site.admin_view(get_kvartal_info), name="get-kvartal-info"),
            url(r'^get-region-info/$', admin.site.admin_view(get_region_info), name="get-region-info"),
            url(r'^get-kvartal/$', MapLayer.as_view(model=GeoKvartal,properties=('number','id')), name='mushrooms'),
            url(ur'^get-polygon-json$',  GetPolygonJson.as_view(model=GeoPolygon,properties=('id',)), name='get-poligon-json'),
            url(ur'^get-polygon-json-firerisk$',  GetPolygonJsonFirerisk.as_view(model=GeoPolygon,properties=('id','class_risk2',))),
        )

        return my_urls + urls
admin.site.register(ValueParamPolygon, ValueParamPolygonAdmin)


def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            url(r'^sections/$', admin.site.admin_view(sections)),
            url(r'^regions/$', admin.site.admin_view(regions)),
            url(r'^risk/(?P<risk>\w+)$', admin.site.admin_view(risk)),
            url(r'^get-kvartal-info/$', admin.site.admin_view(get_kvartal_info), name="get-kvartal-info"),
            url(r'^get-region-info/$', admin.site.admin_view(get_region_info), name="get-region-info"),
            url(r'^get-kvartal/$', MapLayer.as_view(model=GeoKvartal,properties=('number','id')), name='mushrooms'),
            url(ur'^get-polygon-json$',  GetPolygonJson.as_view(model=GeoPolygon,properties=('id',)), name='get-poligon-json'),
            url(ur'^get-polygon-json-firerisk$',  GetPolygonJsonFirerisk.as_view(model=GeoPolygon,properties=('id','class_risk2',))),
        )
        return my_urls + urls
    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
  


