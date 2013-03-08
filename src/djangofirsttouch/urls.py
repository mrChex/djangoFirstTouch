# -*- coding: utf-8 -8-
from django.conf.urls import patterns, include, url
from django.conf import settings
#from registration.forms import RegistrationFormUniqueEmail
from splash import views as splash_views
from registration.forms import RegistrationForm

urlpatterns = patterns('',
                       url(r'^$', 'djangofirsttouch.views.index'),
                       #url(r'^$', splash_views.Splash.as_view()),
                       (r'^account/', include('account.urls')),
                       #Uncomment the next line to enable the admin:
                       #(r'^admin/', include(admin.site.urls)),
                       url(r'^account/register/$', 'registration.views.form'),# {'form': RegistrationFormUniqueEmail}, name='registration_register'),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
                            )


