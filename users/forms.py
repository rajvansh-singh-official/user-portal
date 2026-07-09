from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Document, Interview

class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
class DocumentForm(forms.ModelForm):
    
    class Meta:
        
        model = Document
        
        fields = [
            "title",
            "file"
            ]
        
class InterviewForm(forms.ModelForm):
    
    class Meta:
        
        model = Interview
        
        fields = [
            "scheduled_at",
            "interviewer",
            "mode",
            "interview_round",
            "notes"
            ]
        
class InterviewScheduleForm(forms.ModelForm):
    
    class Meta:
        
        model = Interview
        
        fields = [
            "user",
            "scheduled_at",
            "interviewer",
            "mode",
            "interview_round",
            "notes"
            ]