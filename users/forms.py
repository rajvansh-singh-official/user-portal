from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django import forms
class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)