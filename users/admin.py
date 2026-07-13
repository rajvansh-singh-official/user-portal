from django.contrib import admin
from .models import Document, Interview, Question, Option

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    
    list_display = (
        "id",
        "question_type",
        "difficulty",
        "marks",
        "is_active",
    )

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    
    list_display = (
        "id",
        "question",
        "option_text",
        "is_correct",
    )