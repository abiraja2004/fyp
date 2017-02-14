from django.conf.urls import *
from django.conf.urls import include, url
from django.contrib import admin
from news.views import hello_world, politics, finance, post_detail, home
from news import opinion_search
from news import opinion_search_2
from news import timeline

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/$', hello_world),
	url(r'^$', home),
	url(r'^politics/$', politics),
	url(r'^finance/$', finance),
	url(r'^news/(?P<pk>\d+)/$',post_detail, name='post_detail'),
	url(r'^search/', include('haystack.urls')),
	url(r'^search-form/$', opinion_search.search_form),
	url(r'^opinion_search/$', opinion_search.search),
	url(r'^search-post/$', opinion_search_2.search_post),
        url(r'^timeline/$', timeline.search_post),
]
