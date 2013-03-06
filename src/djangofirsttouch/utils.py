# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader

def render_to(template=None):
    def renderer(function):
        def wrapper(self, request, *args, **kwargs):
            output = function(self, request, *args, **kwargs)
            t = loader.get_template(template)
            return HttpResponse(t.render(RequestContext(request, output)))

        return wrapper
    return renderer