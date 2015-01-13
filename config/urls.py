from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.site.index_template = 'admin/custom_index.html'
admin.autodiscover()
from forestry.admin import admin_urls, sections, regions, risk, get_kvartal_info, get_region_info, MapLayer, GetPolygonJson, GetPolygonJsonFirerisk
from forestry.models import GeoKvartal, GeoPolygon


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'config.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sections/$', sections),
    url(r'^regions/$', regions),
    url(r'^risk/(?P<risk>\w+)$', risk),
    url(r'^get-kvartal-info/$', get_kvartal_info, name="get-kvartal-info"),
    url(r'^get-region-info/$', get_region_info, name="get-region-info"),
    url(r'^get-kvartal/$', MapLayer.as_view(model=GeoKvartal,properties=('number','id')), name='mushrooms'),
    url(ur'^get-polygon-json$',  GetPolygonJson.as_view(model=GeoPolygon,properties=('id',)), name='get-poligon-json'),
    url(ur'^get-polygon-json-firerisk$',  GetPolygonJsonFirerisk.as_view(model=GeoPolygon,properties=('id','class_risk2',))),
    url(r'^', include(admin.site.urls)),
)

#admin.site.get_urls = admin_urls
