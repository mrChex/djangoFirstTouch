from django.shortcuts import render_to_response
from registration.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms as forms
from django.contrib.auth.forms import UserCreationForm

def form(request):
    form = UserCreationForm()
    return render_to_response('registration/registration_form.html', {'form': form})

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/account/login")
    else:
        data, errors = {}, {}

    return render_to_response("registration/registration_complete.html", {
        'form' : forms.FormWrapper(form, data, errors)
    })