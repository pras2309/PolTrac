# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from registration.models import User

from registration.registration_form import RegistrationForm 

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RegistrationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            post_data = request.POST
            import ipdb;ipdb.set_trace()
            rec = User(username=post_data["username"],
                               first_name=post_data["first_name"],
                               last_name=post_data['last_name'],
                               email=post_data['email'],
                               date_of_birth=post_data['dob_dd']+'/'+post_data['dob_mm']+'/'+post_data['dob_yy'],
                               sex=post_data['sex'])
            rec.save()
            return HttpResponseRedirect('/registration/list/') # Redirect after POST
    else:
        form = RegistrationForm() # An unbound form

    return render(request, 'registration/registration.html', {
        'form': form,
    })    
    

def list(request):
    records = User.objects.all()
    #import ipdb;ipdb.set_trace()
    rec_count = User.objects.count()
#     import ipdb;ipdb.set_trace()
    return render(request, 'registration/list.html', {
        'records': records,
        'rec_count': int(rec_count)
    })
    
def profile(request, id):
    #import ipdb;ipdb.set_trace()
    record = User.objects.get(id=id)
    return render(request, 'registration/profile.html', {
        'record': record,
    })    