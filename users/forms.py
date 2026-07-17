from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Document, Interview, Question, Option, Category

# ===== SHARED WIDGETS =====

INTERVIEW_WIDGETS = {
    "scheduled_at": forms.DateTimeInput(
        attrs={
            "type": "datetime-local",
        },
        format="%Y-%m-%dT%H:%M",
    ),
    
    "notes": forms.Textarea(
        attrs={
            "rows": 4,
        }
    ),
}

# ===== AUTHENTICATION =====

class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)

# ===== DOCUMENTS =====

class DocumentForm(forms.ModelForm):
    
    class Meta:
        
        model = Document
        
        fields = [
            "title",
            "file"
            ]
        
# ===== INTERVIEWS =====
        
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
        
        widgets = INTERVIEW_WIDGETS  
        
# ===== QUESTIONS =====

class QuestionForm(forms.ModelForm):
    
    class Meta:
        
        model = Question
        
        fields = [
            "question_text",
            "question_type",
            "category",
            "difficulty",
            "marks",
            "is_active",
        ]
        
        widgets = {
            "question_type": forms.Select(
                attrs={
                    "id": "question-type"
                }
            ),
        }
        
class OptionForm(forms.ModelForm):
    
    class Meta:
        
        model = Option
        
        fields = [
            "option_text",
            "is_correct",
        ]
        
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["name"]

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(
                "Category already exists."
            )

        return name.title()