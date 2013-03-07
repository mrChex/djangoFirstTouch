from django.shortcuts import render_to_response
from registration.forms import RegistrationForm

def register(request, success_url=None,
             form_class=RegistrationForm,
             #form_class=RegistrationFormUniqueEmail,
             profile_callback=None,
             template_name='registration/registration_form.html',
             extra_context=None):

    if request.method == "POST":
        uform = RegistrationForm(data = request.POST)
        pform = RegistrationForm(data = request.POST)
        eform = RegistrationForm(data = request.POST)
        if uform.is_valid() and pform.is_valid() and eform.is_valid():
            user = uform.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()
        else:
            render_to_response("/")

    return render_to_response("registration/registration_form.html", )

def index(request):
    return render_to_response("index.html")

def add_user(request):
    return render_to_response("registration/registration_complete.html")