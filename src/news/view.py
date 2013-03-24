# -*- coding: utf-8 -*-
from django.views.generic import View
from djangofirsttouch.utils import render_to


class News(View):

    @render_to('json')
    def get(self, request):
        return {
            "news": [
                {"id": 1,
                 "title": "Наша первая новость",
                 "text": "Это тело нашей новости"},

                {"id": 2,
                 "title": "Это наша вторая новость",
                 "text": "Это тело нашей второй новости"},

                {"id": 3,
                 "title": "ТРЕТЬЯ НОВОСТЬ",
                 "text": "ЕБАТЬ!!!! Все работает само собой!!! ЕБАТЬ!!!!!"}
            ][::-1]
        }