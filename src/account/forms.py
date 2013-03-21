# -*- coding: utf-8 -*-
from django import forms as forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, label=(u'Password'), widget=forms.PasswordInput)

    def clean_username(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        return user

    def clean_password(self):
        user = self.cleaned_data['username'] # User object
        password = self.cleaned_data['password'] # String

        if user.check_password(password):
            return password
        else:
            raise forms.ValidationError("Wrong password")
