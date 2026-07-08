from django.db import models
from django.contrib.auth.models import User


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
        choices=STATUS_CHOICES
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.interview_round}"