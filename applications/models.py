from django.db import models
from django.conf import settings
from jobs.models import Job

class Application(models.Model):
    APPLIED = "applied"
    REVIEWING = "reviewing"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

    STATUS_CHOICES = [
        (APPLIED, "Applied"),
        (REVIEWING, "Reviewing"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    cv = models.FileField(upload_to="applications/cv/")
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=APPLIED)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "job")  # Prevent applying twice

    def __str__(self):
        return f"{self.user.email} -> {self.job.title}"
