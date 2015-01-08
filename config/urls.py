from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.site.index_template = 'admin/custom_index.html'
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'config.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
