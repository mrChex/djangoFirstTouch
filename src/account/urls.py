# -*- coding: utf-8 -8-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout



urlpatterns = patterns('',
                       (r'^login/$',  login),
                       (r'^logout/$', logout),
                       )