# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from registration.registration_form import RegistrationForm 

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RegistrationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = RegistrationForm() # An unbound form

    return render(request, 'registration/registration.html', {
        'form': form,
    })    
    
    return HttpResponse("Hello, world. You're at the registration")