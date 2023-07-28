from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Appointment model
SERVICE_CHOICES = (
    ("General care doctor", "General care doctor"),
    ("General surgery", "General surgery"),
    ("Family medicine", "Family medicine"),
    ("Emergency medicine", "Emergency medicine"),
    ("Cardiology", "Cardiology"),
    ("Obstetrics and gynaecology", "Obstetrics and gynaecology"),
    ("Dermatology", "Dermatology")
    )
TIME_CHOICES = (
    ("12 PM", "12 PM"),
    ("12:30 PM", "12:30 PM"),
    ("2 PM", "2 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM")
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
