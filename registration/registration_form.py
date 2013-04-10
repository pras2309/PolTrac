from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    date_of_birth = forms.CharField(max_length=200)