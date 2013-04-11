from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    dob_dd = forms.CharField(max_length=200)
    dob_mm = forms.CharField(max_length=200)
    dob_yy = forms.CharField(max_length=4,)    
    sex = forms.ChoiceField(widget = forms.Select(), 
                 choices = ([('M','M'), ('F','F'), ]), required = True,)