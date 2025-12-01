# jobs/models.py
from django.db import models
from django.conf import settings
from django.contrib.postgres.search import SearchVectorField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class JobType(models.TextChoices):
    FULL_TIME = "FT", "Full time"
    PART_TIME = "PT", "Part time"
    CONTRACT = "CT", "Contract"
    REMOTE = "RE", "Remote"

class Job(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, unique=True)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.JSONField(default=list, blank=True)   # array of strings
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=2, choices=JobType.choices)
    category = models.ForeignKey(Category, related_name="jobs", on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=128, blank=True)
    is_remote = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posted_jobs", on_delete=models.SET_NULL, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # tsvector column for full-text search (managed via migration or trigger)
    search_vector = SearchVectorField(null=True, editable=False)

    class Meta:
        indexes = [
            models.Index(fields=['is_active', 'posted_at']),
            models.Index(fields=['category']),
            models.Index(fields=['job_type']),
            models.Index(fields=['city']),
        ]

    def __str__(self):
        return f"{self.title} @ {self.company_name}"
