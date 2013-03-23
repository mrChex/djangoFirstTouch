from django.views.generic import View

from djangofirsttouch.utils import render_to
from blog.forms import Blog

class Blog(View):

    @render_to("blog/blog.jinja")
    def get(self, request):
        return {}
