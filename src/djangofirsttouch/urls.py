# -*- coding: utf-8 -8-
from django.conf.urls import patterns, include, url
from django.conf import settings
from registration.forms import RegistrationFormUniqueEmail
from splash import views as splash_views

urlpatterns = patterns('',
                       url(r'^$', splash_views.Splash.as_view()),
                       (r'^accounts/', include('registration.urls')),
                       #Uncomment the next line to enable the admin:
                       #(r'^admin/', include(admin.site.urls)),
                       url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
                       url('', include('registration.urls')),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
                            )


