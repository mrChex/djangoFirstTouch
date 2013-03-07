from django.shortcuts import render_to_response
from django.forms import RegistrationFormUniqueEmail

def register(request, success_url=None,
             #form_class=RegistrationForm,
             form_class=RegistrationFormUniqueEmail,
             profile_callback=None,
             template_name='registration/registration_form.html',
             extra_context=None):
    return render_to_response("registration/registration_form.html", data)

def addUser(request):
    return render_to_response("registration/activate.html")