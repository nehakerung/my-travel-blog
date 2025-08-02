from django.db import models


class Attendance(models.TextChoices):
    """Choices of who attended the trip with Neha."""

    SOLO = "Solo"
    FAMILY = "Family"
    SISTER = "Sister"
    FRIENDS = "Friends"
