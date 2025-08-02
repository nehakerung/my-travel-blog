from django.db import models
from django.utils import timezone

from .enums import Attendance


class Trip(models.Model):
    """Trip."""

    country = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    attendance = models.CharField(
        max_length=10,
        choices=Attendance.choices,
        default=Attendance.SOLO,
    )
    intro_text = models.CharField(max_length=300)
    main_image = models.ImageField(blank=True, upload_to="images/")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.country} ({self.start_date} - {self.end_date})"
