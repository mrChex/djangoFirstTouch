# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model, SESSION_KEY
from django.contrib.auth.signals import user_logged_in, user_logged_out

from djangofirsttouch.utils import render_to
from account.forms import LoginForm


class Profile(View):

    @render_to("account/profile.jinja")
    def get(self, request):
        return {}


class Login(View):

    @render_to("account/login.jinja")
    def get(self, request):
        if request.user.is_authenticated():
            return {"redirect": "/account/profile/"}

        form = LoginForm()
        return {'form': form}

    @render_to("account/login.jinja")
    def post(self, request):
        form = LoginForm(request.POST.copy())

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data['username'], password=data['password'])
            if user:
                auth_login(request, user)
                return {"redirect": "/account/profile/"}

        return {'form': form}


class Logout(View):

    @render_to(None)
    def get(self, request):
        auth_logout(request)
        return {"redirect": "/account/login/"}