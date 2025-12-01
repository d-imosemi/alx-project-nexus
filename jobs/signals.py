# jobs/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector
from .models import Job

# update the search vector when a job is saved
@receiver(post_save, sender=Job)
def update_search_vector(sender, instance, **kwargs):
    Job.objects.filter(pk=instance.pk).update(
        search_vector=(
            SearchVector('title', weight='A') +
            SearchVector('company_name', weight='B') +
            SearchVector('description', weight='C')
        )
    )
