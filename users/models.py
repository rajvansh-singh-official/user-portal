from django.db import models
from django.contrib.auth.models import User

# ===== DOCUMENTS =====

class Document(models.Model):

    title = models.CharField(max_length=60)

    file = models.FileField(upload_to="documents/")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# ===== INTERVIEWS =====
    
class Interview(models.Model):

    MODE_CHOICES = [
        ("online", "Online"),
        ("offline", "Offline"),
    ]

    ROUND_CHOICES = [
        ("technical", "Technical"),
        ("hr", "HR"),
        ("managerial", "Managerial"),
        ("final", "Final"),
    ]

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("rescheduled", "Rescheduled"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="interviews"
    )

    scheduled_at = models.DateTimeField()

    interviewer = models.CharField(max_length=100)

    mode = models.CharField(
        max_length=10,
        choices=MODE_CHOICES
    )

    interview_round = models.CharField(
        max_length=20,
        choices=ROUND_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="scheduled"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.interview_round}"
    
# ===== QUESTIONS =====

class Category(models.Model):
    
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    
    QUESTION_TYPE_CHOICES = [
        ("mcq", "MCQ"),
        ("true_false", "True False"),
        ("short_answer", "Short Answer"),
        ("long_answer", "Long Answer"),
    ]
    
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]
    
    question_text = models.TextField()
    
    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPE_CHOICES,
        default="mcq"
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="questions",
    )
    
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
    )
    
    marks = models.PositiveIntegerField()
    
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.question_type} - {self.question_text[:40]}"
    
class Option(models.Model):
    
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="options"
    )
    
    option_text = models.TextField()
    
    is_correct = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.option_text[:40]