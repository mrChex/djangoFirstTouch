from django.conf.urls import patterns, include, url

from news import view

urlpatterns = patterns('',
                       (r'^/$',  view.News.as_view()),
              )