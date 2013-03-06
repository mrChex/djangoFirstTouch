# -*- coding: utf-8 -8-
from django.conf.urls import patterns, include, url
from django.conf import settings

from splash import views as splash_views

urlpatterns = patterns('',
                       url(r'^$', splash_views.Splash.as_view()),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
