from django.contrib import admin
from .models import Document, Interview

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass