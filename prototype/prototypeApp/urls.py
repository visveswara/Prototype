from django.conf.urls import patterns, include, url
from prototypeApp import views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'prototype.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^$', views.index, name='index'),
# )

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)