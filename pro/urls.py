from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf	import settings
from django.contrib import comments
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KOJ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   
)
urlpatterns+=patterns((''),
	(r'^oj/',include('oj.urls')),
	)
#urls to other urls.py
urlpatterns+=patterns((''),
	(r'static/(?P<path>.*)','django.views.static.serve',
		{'document_root':settings.STATIC_ROOT}
		),
	)