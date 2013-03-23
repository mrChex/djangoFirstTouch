from django.views.generic import View

from djangofirsttouch.utils import render_to

class Blog(View):

    @render_to("blog/blog.jinja")
    def get(self, request):
        return {}
