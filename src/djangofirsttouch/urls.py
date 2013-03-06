# -*- coding: utf-8 -8-
from django.conf.urls import patterns, include, url

from splash import views as splash_views

urlpatterns = patterns('',
    url(r'^$', splash_views.Splash.as_view()),
)
