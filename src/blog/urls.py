from django.conf.urls import patterns, include, url

from blog import views as blog_views

urlpatterns = patterns('',

                       (r'^blog/$',  blog_views.Blog.as_view()),

                      )