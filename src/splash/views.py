# -*- coding: utf-8 -*-
from django.views.generic import View
from djangofirsttouch.utils import render_to


class Splash(View):

    @render_to('splash/splash.jinja')
    def get(self, request):
        return {}
