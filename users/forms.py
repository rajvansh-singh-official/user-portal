from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Document

class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
class DocumentForm(forms.ModelForm):
    
    class Meta:
        
        model = Document
        
        fields = ["title", "file"]