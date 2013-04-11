# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from registration.models import Registration

from registration.registration_form import RegistrationForm 

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RegistrationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            rec = Registration(username='username',
                               first_name='first_name',
                               last_name='last_name',
                               email='email@email.com',
                               date_of_birth='23/09/1981',
                               sex='male')
            rec.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = RegistrationForm() # An unbound form

    return render(request, 'registration/registration.html', {
        'form': form,
    })    
    

def list(request):
    records = Registration.objects.all()
    rec_count = Registration.objects.count()
    return render(request, 'registration/list.html', {
        'records': records,
        'rec_count':rec_count
    })